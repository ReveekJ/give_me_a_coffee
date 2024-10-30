from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from src.db.organizations.crud import OrganizationDB
from src.admin_tgbot.edit_organization.schemas import MainMenuData
from src.admin_tgbot.edit_organization.states import MainMenuSG


async def on_start_main_dialog(dialog_manager: DialogManager, *args, **kwargs):
    if dialog_manager.start_data.get('organization_id') is None:
        raise ValueError('при старте диалога, нужно передать id организации')

    org_id = dialog_manager.start_data.get('organization_id')
    organization = OrganizationDB.get_organization_by_id(org_id)

    dialog_manager.dialog_data['dialog_data_dto'] = MainMenuData(
        organization=organization,
    )


async def select_worker_handler(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, *args, **kwargs):
    dialog_data: MainMenuData = dialog_manager.dialog_data.get('dialog_data_dto')
    dialog_data.selected_worker_id = callback.data

    dialog_manager.dialog_data['dialog_data_dto'] = dialog_data

    await dialog_manager.switch_to(MainMenuSG.actions_with_worker)
