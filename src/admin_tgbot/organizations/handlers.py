import logging

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from src.db.organizations.crud import OrganizationDB
from src.db.organizations.schemas import OrganizationSchema
from src.admin_tgbot.edit_organization.states import MainMenuSG


async def save_name(message: Message, widget: MessageInput, dialog_manager: DialogManager, *args, **kwargs) -> None:
    organization = OrganizationSchema(
        name=message.text,
        owner_id=message.from_user.id,
    )
    org_id = OrganizationDB.create_organization(organization)

    await dialog_manager.done()
    await dialog_manager.start(MainMenuSG.main_menu, data={'organization_id': org_id})


async def go_to_edit_organization(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    await dialog_manager.done()
    await dialog_manager.start(MainMenuSG.main_menu, data={'organization_id': callback.data.split(':')[-1]})
