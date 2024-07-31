import asyncio
import logging
from re import Match

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.config import settings

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(f"👋 {message.from_user.full_name}")


@dp.message(F.text.regexp(r"^reply:(.+)$").as_("text"))
async def reply_handler(message: Message, text: Match[str]) -> None:
    await message.reply(text.group(1))


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.copy_to(chat_id=message.chat.id)


async def main() -> None:
    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
