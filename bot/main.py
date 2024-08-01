import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from aiogram.utils.chat_action import ChatActionMiddleware

from bot.config import settings
from bot.handlers import router
from bot.middlewares import CounterMiddleware


async def main() -> None:
    dp = Dispatcher()
    dp.message.outer_middleware(CounterMiddleware())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router)

    @dp.error(ExceptionTypeFilter(ValueError))
    async def value_error_handler(error: ErrorEvent) -> None:
        print(f"ValueError was handled: {error.exception}")

    bot = Bot(token=settings.bot_token)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
