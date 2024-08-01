import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

from bot.config import settings
from bot.handlers import router
from bot.middlewares import CounterMiddleware


async def main() -> None:
    dp = Dispatcher()
    dp.message.outer_middleware(CounterMiddleware())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router)

    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
