from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput

from src.db.organizations.crud import OrganizationDB
from src.db.organizations.schemas import OrganizationSchema
from src.admin_tgbot.edit_organization.states import MainMenuSG


async def save_name(message: Message, widget: MessageInput, dialog_manager: DialogManager, *args, **kwargs):
    dialog_manager.show_mode =ShowMode.DELETE_AND_SEND

    organization = OrganizationSchema(
        name=message.text,
        owner_id=message.from_user.id,
    )
    org_id = OrganizationDB.create_organization(organization)

    await dialog_manager.done()
    await dialog_manager.start(MainMenuSG.main_menu, data={'organization_id': org_id})
