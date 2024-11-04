from aiogram.types import User
from aiogram_dialog import DialogManager

from src.db.organizations.crud import OrganizationDB


async def organizations_getter(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    organizations = OrganizationDB.get_organization_by_owner_id(event_from_user.id)

    return {'organizations_list': [(i.id, i.name) for i in organizations]}
