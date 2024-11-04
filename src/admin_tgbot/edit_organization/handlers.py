from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button

from src.admin_tgbot.edit_organization.schemas import MainMenuData
from src.admin_tgbot.edit_organization.states import MainMenuSG
from src.db.workers.crud import WorkersDB
from src.utils.aiogram_dialogs_utils import get_dialog_data_dto


async def on_start_main_dialog(start_data: dict, dialog_manager: DialogManager, *args, **kwargs):
    if start_data.get('organization_id') is None:
        raise ValueError('при старте диалога, нужно передать id организации')

    org_id = start_data.get('organization_id')

    dialog_manager.dialog_data['dialog_data_dto'] = MainMenuData(
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

    WorkersDB.delete_worker(dialog_data.selected_worker_id)

    await callback.message.answer("Работник успешно удален")
    await dialog_manager.switch_to(MainMenuSG.list_of_workers)
