from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager

from src.admin_tgbot.organizations.states import OrganizationSG
from src.db.organizations.crud import OrganizationDB
from src.db.owners.crud import OwnerDB
from src.db.owners.schemas import OwnerSchema
from src.db.workers.crud import WorkersDB
from src.db.workers.schemas import WorkerSchema

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    txt = message.text.split()[-1]

    if txt == '/start':
        return None

    match txt.split('_')[0]:
        case 'worker':
            worker = WorkerSchema(
                id=message.from_user.id,
                name=f'{message.from_user.first_name} {message.from_user.last_name}',
                username=message.from_user.username,
                organization_id=int(txt.split('_')[-1])
            )

            WorkersDB.create_worker(worker)

            organization = OrganizationDB.get_organization_by_id(int(txt.split('_')[-1]))
            await message.answer(f'Ты успешно присоединился(-ась) к организации "{organization.name}"')
        case 'user':
            pass
