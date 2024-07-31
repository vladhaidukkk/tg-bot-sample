import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

from bot.config import settings
from bot.handlers import router


async def main() -> None:
    dp = Dispatcher()
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router)

    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
