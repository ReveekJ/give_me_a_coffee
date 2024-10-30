from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Select, Group, Back
from aiogram_dialog.widgets.text import Format, Multi

from src.admin_tgbot.edit_organization.getters import workers_getter, add_workers_getter
from src.admin_tgbot.edit_organization.handlers import on_start_main_dialog, select_worker_handler
from src.admin_tgbot.edit_organization.states import MainMenuSG

edit_organization_dialog = Dialog(
    Window(
        Format('основное меню'),
        SwitchTo(
            Format('Изменить работников'),
            id='change_workers',
            state=MainMenuSG.list_of_workers
        ),
        state=MainMenuSG.main_menu
    ),
    Window(
        Format('Здесь вы можете изменить работников организации'),
        Group(
            Select(
                Format('{item[1]}'),
                id='workers_list',
                item_id_getter=lambda item: item[0],
                items='workers',
                on_click=select_worker_handler,
            ),
            width=1
        ),
        SwitchTo(
            text=Format('Добавить работников'),
            id='switch_to_add_workers',
            state=MainMenuSG.add_workers
        ),
        Back(
            text=Format('Назад')
        ),
        getter=workers_getter,
        state=MainMenuSG.list_of_workers
    ),
    Window(
        Multi(
            Format('Отправьте эту ссылку вашим работникам и они присоединятся к вашей организации\n\n'),
            Format('{link}'),
        ),
        Back(
            text=Format('Назад')
        ),
        getter=add_workers_getter,
        state=MainMenuSG.add_workers
    ),
    Window(
        state=MainMenuSG.actions_with_worker
    ),
    on_start=on_start_main_dialog
)