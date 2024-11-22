import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram_dialog import setup_dialogs

from src.admin_tgbot.edit_organization.dialogs import edit_organization_dialog, edit_menu_dialog, location_dialog
from src.admin_tgbot.organizations.dialogs import organization_dialog
from src.admin_tgbot.start_command import start_router
from src.config import TOKEN_ADMIN

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN_ADMIN)

    dp.include_routers(start_router, organization_dialog, edit_organization_dialog, edit_menu_dialog, location_dialog)

    setup_dialogs(dp)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    asyncio.run(main())
