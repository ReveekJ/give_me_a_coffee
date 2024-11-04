from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Select, SwitchTo, Back
from aiogram_dialog.widgets.text import Format

from src.admin_tgbot.organizations.getters import organizations_getter
from src.admin_tgbot.organizations.handlers import save_name, go_to_edit_organization
from src.admin_tgbot.organizations.states import OrganizationSG

organization_dialog = Dialog(
    Window(
        Format('Выбери организацию для редактирования или создай новую'),
        Group(
            Select(
                Format('{item[1]}'),
                id='organizations_list',
                item_id_getter=lambda x: x[0],
                items='organizations_list',
                on_click=go_to_edit_organization,
            ),
            width=1
        ),
        SwitchTo(
            text=Format('Создать организацию'),
            id='create',
            state=OrganizationSG.ask_name,
        ),
        getter=organizations_getter,
        state=OrganizationSG.select_organization,
    ),
    Window(
        Format('Введи название организации'),
        MessageInput(
            func=save_name,
            content_types=ContentType.TEXT
        ),
        Back(
            text=Format('Назад')
        ),
        state=OrganizationSG.ask_name
    ),
)
