from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Format

from src.admin_tgbot.organizations.handlers import save_name
from src.admin_tgbot.organizations.states import OrganizationSG

organization_dialog = Dialog(
    Window(
        Format()
    ),
    Window(
        Format('Введи название организации'),
        MessageInput(
            func=save_name,
            content_types=ContentType.TEXT
        ),
        state=OrganizationSG.ask_name
    ),
)
