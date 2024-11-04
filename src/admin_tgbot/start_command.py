from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager

from src.admin_tgbot.organizations.states import OrganizationSG
from src.db.owners.crud import OwnerDB
from src.db.owners.schemas import OwnerSchema

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    owner = OwnerSchema(id=message.from_user.id)
    print(owner)
    if OwnerDB.get_owner_by_id(owner.id) is None:
        print('я тут')
        OwnerDB.create_owner(owner)

    await dialog_manager.start(OrganizationSG.select_organization)
