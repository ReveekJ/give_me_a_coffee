import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram_dialog import setup_dialogs

from src.user_tgbot.start_command import start_router
from src.config import TOKEN_USER

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN_USER)

    dp.include_routers(start_router)

    setup_dialogs(dp)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    asyncio.run(main())
