from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters import Admin

router = Router(name=__name__)


@router.message(Command("admin"), Admin())
async def admin_command_handler(message: Message) -> None:
    await message.answer(f"👑 Admin <b>{message.from_user.username}</b>")
