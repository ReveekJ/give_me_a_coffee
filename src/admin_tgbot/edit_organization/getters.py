from aiogram.types import User
from aiogram_dialog import DialogManager

from src.admin_tgbot.edit_organization.schemas import MainMenuData


async def workers_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs) -> dict:
    dialog_data: MainMenuData = dialog_manager.dialog_data.get('dialog_data_dto')

    return {'workers': [(i.id, f'{i.name} ({i.username})'[:20]) for i in dialog_data.organization.workers]}


async def add_workers_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs) -> dict:
    dialog_data: MainMenuData = dialog_manager.dialog_data.get('dialog_data_dto')

    return {'link': f'https://t.me/give_me_a_coffee_please_bot?start={dialog_data.organization.id}'}
