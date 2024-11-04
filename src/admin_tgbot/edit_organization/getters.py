from aiogram.types import User
from aiogram_dialog import DialogManager

from src.admin_tgbot.edit_organization.schemas import MainMenuData
from src.db.organizations.crud import OrganizationDB
from src.db.workers.crud import WorkersDB
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto


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
