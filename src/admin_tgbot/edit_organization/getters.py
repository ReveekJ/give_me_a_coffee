from aiogram.enums import ContentType
from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from aiogram_dialog.widgets.kbd import ManagedMultiselect

from src.admin_tgbot.edit_organization.schemas import MainMenuData, EditMenuData, LocationsData
from src.db.locations.crud import LocationsDB
from src.db.menu.crud import FoodDB, IngredientsDB
from src.db.organizations.crud import OrganizationDB
from src.db.possible_ingredients.crud import PossibleIngredientsDB
from src.db.workers.crud import WorkersDB
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto, list_to_select_format
from src.utils.qr_code_generator import generate_qr


async def workers_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs) -> dict:
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)
    organization = OrganizationDB.get_organization_by_id(dialog_data.organization_id)

    return {'workers': [(i.id, f'{i.name} (@{i.username})'[:20]) for i in organization.workers]}


async def add_workers_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs) -> dict:
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)

    return {'link': f'https://t.me/give_me_a_coffee_please_bot?start=worker_{dialog_data.organization_id}'}


async def actions_with_worker_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)
    worker = WorkersDB.get_worker_by_id(dialog_data.selected_worker_id)

    return {'worker_name': f'{worker.name} (@{worker.username})'}


async def foods_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)

    foods = FoodDB.get_foods_by_organization_id(dialog_data.organization_id)

    return {'food_groups': [(i.id, i.name) for i in foods]}


async def ingredients_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: EditMenuData = get_dialog_data_dto(dialog_manager)
    ingredients = IngredientsDB.get_ingredients_by_organization_id(dialog_data.organization_id)

    # Выставляем выбранные ингредиенты
    possible_ingredients_for_food = PossibleIngredientsDB.get_possible_ingredients_by_food_id(dialog_data.selected_food_id)
    ingredients_multiselect: ManagedMultiselect = dialog_manager.find('ingredients_multiselect')

    for possible_ingredient in possible_ingredients_for_food:
        await ingredients_multiselect.set_checked(possible_ingredient, True)
    for impossible_ingredient in [i.id for i in ingredients if i.id not in possible_ingredients_for_food]:
        await ingredients_multiselect.set_checked(impossible_ingredient, False)

    return {'ingredients': [(i.id, i.name) for i in ingredients]}


async def qr_code_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: MainMenuData = get_dialog_data_dto(dialog_manager)
    link = f'https://t.me/give_me_a_coffee_please_bot?start=user_{dialog_data.organization_id}_{dialog_data.selected_location_for_qr}'
    path_to_qr = generate_qr(link)

    return {'link': link,
            'qr_code': MediaAttachment(ContentType.PHOTO, path=path_to_qr)}


async def locations_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    dialog_data: LocationsData = get_dialog_data_dto(dialog_manager)
    locations = LocationsDB.get_locations_by_organization_id(dialog_data.organization_id)

    return {'locations': [(i.id, i.name) for i in locations]}
