import asyncio
import logging
from pprint import pprint

from aiogram import Dispatcher, Bot, Router
from aiogram.types import Message

from src.config import Settings


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

router = Router()


@router.message()
async def test(message: Message, **kwargs):
    pprint(message.text)
    pprint(kwargs)


@router.callback_query()
async def test2(*args, **kwargs):
    pprint(args)
    pprint(kwargs)


async def main():
    dp = Dispatcher()
    bot = Bot(token=Settings().TOKEN)

    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    asyncio.run(main())


