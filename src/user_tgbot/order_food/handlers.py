import asyncio

from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect

from src.db.locations.crud import LocationsDB
from src.db.menu.crud import FoodDB
from src.db.task_ingredients.crud import TaskIngredientsDB
from src.db.tasks.crud import TaskDB
from src.db.tasks.schemas import TaskSchema
from src.db.workers.crud import WorkersDB
from src.user_tgbot.order_food.schemas import OrderFoodData
from src.user_tgbot.order_food.states import OrderFoodSG
from src.user_tgbot.worker_part.keyboards import WorkerKeyboards
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto
from src.utils.order_food_utils import get_text_of_order
from src.utils.task_messages_redis import TaskMessagesRedis, TaskMessageSchema


async def on_start_order_food_dialog(start_data: dict, dialog_manager: DialogManager, *args, **kwargs):
    if start_data.get('organization_id') is None or start_data.get('location_id') is None:
        raise ValueError('при старте диалога, нужно передать id организации и локации')

    org_id = start_data.get('organization_id')
    location_id = start_data.get('location_id')
    dialog_manager.dialog_data['dialog_data_dto'] = OrderFoodData(
        organization_id=org_id,
        location_id=location_id
    )


async def select_food_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)
    dialog_data.food_id = callback.data.split(':')[-1]
    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(OrderFoodSG.select_ingredients)


async def select_ingredients_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)
    ingredients_multiselect: ManagedMultiselect = dialog_manager.find('ingredients_multiselect')

    dialog_data.ingredients_ids = ingredients_multiselect.get_checked()
    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(OrderFoodSG.approve_food)



async def make_order_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: OrderFoodData = get_dialog_data_dto(dialog_manager)

    order = TaskSchema(
        organization_id=dialog_data.organization_id,
        food_id=dialog_data.food_id,
        location_id=dialog_data.location_id
    )
    task_id = TaskDB.create_task(order)
    TaskIngredientsDB.create_link_task_ingredients(task_id, dialog_data.ingredients_ids)

    # рассылка по работникам
    bot = callback.bot
    location = LocationsDB.get_location_by_id(dialog_data.location_id)
    order_text = f'Новый заказ от {callback.from_user.first_name} {callback.from_user.last_name} (@{callback.from_user.username}) в локацию "{location.name}"\n\n{get_text_of_order(dialog_data)}'
    message_ids = []

    for worker in WorkersDB.get_workers_by_organization_id(dialog_data.organization_id):
        try:
            msg = await bot.send_message(chat_id=worker.id, text=order_text, reply_markup=WorkerKeyboards.take_on_job(task_id))
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            msg = await bot.send_message(chat_id=worker.id, text=order_text, reply_markup=WorkerKeyboards.take_on_job(task_id))
        except TelegramForbiddenError:
            continue  # работник заблокировал бота

        message_ids.append(
            TaskMessageSchema(
                chat_id=worker.id,
                message_id=msg.message_id,
            )
        )

    async with TaskMessagesRedis() as redis:
        await redis.create_task_messages(task_id, message_ids)

    # уведомляем пользователя о том, что заказ оформлен
    food = FoodDB.get_food_by_id(dialog_data.food_id)
    await dialog_manager.done()
    await callback.message.edit_text(text=f'Заказ оформлен. Скоро к вам подойдет сотрудник и принесет {food.name}\nЧтобы сделать еще один заказ, отсканируйте QR снова')
