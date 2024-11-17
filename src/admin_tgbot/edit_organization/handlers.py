from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect

from src.admin_tgbot.edit_organization.schemas import MainMenuData, EditMenuData
from src.admin_tgbot.edit_organization.states import MainMenuSG, EditMenuSG
from src.admin_tgbot.organizations.states import OrganizationSG
from src.db.menu.crud import FoodDB, IngredientsDB
from src.db.menu.schemas import FoodSchema, IngredientSchema
from src.db.possible_ingredients.crud import PossibleIngredientsDB
from src.db.workers.crud import WorkersDB
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto


async def back_to_organizations(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)

    await dialog_manager.done()
    await dialog_manager.start(OrganizationSG.select_organization, data={'organization_id': dialog_data.organization_id})


async def back_to_main_menu_of_edit_organization(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    await dialog_manager.done()
    # await dialog_manager.start(MainMenuSG.main_menu)


async def go_to_edit_menu(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)

    await dialog_manager.start(EditMenuSG.select_food, data={'organization_id': dialog_data.organization_id})


async def on_start_main_dialog(start_data: dict, dialog_manager: DialogManager, *args, **kwargs):
    if start_data.get('organization_id') is None:
        raise ValueError('при старте диалога, нужно передать id организации')

    org_id = start_data.get('organization_id')

    dialog_manager.dialog_data['dialog_data_dto'] = MainMenuData(
        organization_id=org_id,
    )

async def on_start_edit_menu_dialog(start_data: dict, dialog_manager: DialogManager, *args, **kwargs):
    if start_data.get('organization_id') is None:
        raise ValueError('при старте диалога, нужно передать id организации')

    org_id = start_data.get('organization_id')

    dialog_manager.dialog_data['dialog_data_dto'] = EditMenuData(
        organization_id=org_id,
    )


async def select_worker_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)
    dialog_data.selected_worker_id = callback.data.split(':')[-1]

    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(MainMenuSG.actions_with_worker)


async def delete_selected_worker(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_manager.show_mode = ShowMode.DELETE_AND_SEND
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)

    try:
        WorkersDB.delete_worker(dialog_data.selected_worker_id)
    except Exception as e:
        await callback.message.answer('Невозможно удалить, вероятно потому что работник еще выполняет какую-то задачу')
        return None

    await callback.message.answer("Работник успешно удален")
    await dialog_manager.switch_to(MainMenuSG.list_of_workers)


async def select_food(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)

    dialog_data.selected_food_id = callback.data.split(':')[-1]
    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(EditMenuSG.choose_action_with_food)


async def save_name_of_food(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)

    food = FoodSchema(
        name=message.text,
        organization_id=dialog_data.organization_id
    )
    food_id = FoodDB.create_food(food)

    dialog_data.selected_food_id = food_id
    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(EditMenuSG.select_ingredient)


async def save_name_of_ingredient(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)

    ingredient = IngredientSchema(
        name=message.text,
        food_id=dialog_data.selected_food_id,
        organization_id=dialog_data.organization_id
    )
    IngredientsDB.create_ingredient(ingredient)

    await dialog_manager.switch_to(EditMenuSG.select_ingredient)


async def process_ingredient_select(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)
    ingredients_multiselect: ManagedMultiselect = dialog_manager.find('ingredients_multiselect')
    clicked_button = str(callback.data.split(':')[-1])

    if not ingredients_multiselect.is_checked(clicked_button):
        PossibleIngredientsDB.create_link_ingredient_food(int(clicked_button), dialog_data.selected_food_id)
    else:
        PossibleIngredientsDB.delete_link_ingredient_food(int(clicked_button), dialog_data.selected_food_id)
    #
    # # удаляем старые возможные ингредиенты
    # PossibleIngredientsDB.delete_link_by_food_id(dialog_data.selected_food_id)
    #
    # # Создаем новые возможные ингредиенты
    # for ingredient_id in ingredients_multiselect.get_checked():
    #     PossibleIngredientsDB.create_link_ingredient_food(ingredient_id, dialog_data.selected_food_id)
    #
    # await dialog_manager.switch_to(EditMenuSG.select_food)
    # IngredientsDB.link_ingredients_with_food(ingredients_multiselect.get_checked(), dialog_data.selected_food_id)
    # IngredientsDB.unlink_ingredients_with_food(ingredients_multiselect(), dialog_data.selected_food_id)

async def delete_food_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)

    FoodDB.delete_food(dialog_data.selected_food_id)

    await dialog_manager.switch_to(EditMenuSG.select_food)
