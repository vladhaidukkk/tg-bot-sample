from aiogram.filters import Filter
from aiogram.types import Message

from bot.config import settings


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in settings.bot_admins
