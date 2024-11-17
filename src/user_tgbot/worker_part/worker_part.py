from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.db.tasks.crud import TaskDB
from src.user_tgbot.worker_part.keyboards import WorkerKeyboards
from src.utils.task_messages_redis import TaskMessagesRedis

router = Router()


@router.callback_query(F.data.startswith('take_on_job'))
async def take_on_job(callback: CallbackQuery):
    task_id = int(callback.data.split(':')[-1])
    # устанавливаем работника
    TaskDB.set_worker_for_task(callback.from_user.id, task_id)

    # меняем клавиатуры у всех работников организации, чтобы никто не смог перехватить задачу
    async with TaskMessagesRedis() as redis:
        messages = await redis.get_task_messages(task_id)

    bot = callback.bot
    for task_message in messages:
        if task_message.message_id != callback.from_user.id:
            await bot.edit_message_reply_markup(chat_id=task_message.chat_id, message_id=task_message.message_id, reply_markup=None)

    # меняем клавиатуру у работника, взявшего задачу (с кнопкой завершить заказ)
    await callback.message.edit_reply_markup(reply_markup=WorkerKeyboards.done_task(task_id))

    await callback.answer()


@router.callback_query(F.data.startswith('done_task'))
async def done_task(callback: CallbackQuery):
    task_id = int(callback.data.split(':')[-1])
    bot = callback.bot

    # удаляем сообщение с заказом у всех работников
    async with TaskMessagesRedis() as redis:
        messages = await redis.get_task_messages(task_id)
        for task_message in messages:
            await bot.delete_message(chat_id=task_message.chat_id, message_id=task_message.message_id)

        # удаляем данные из redis
        await redis.delete_task_messages(task_id)

    # удаляем задачу из бд
    TaskDB.delete_task(task_id)

    await callback.answer()

