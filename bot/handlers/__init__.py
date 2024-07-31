from aiogram import Router

from .commands import router as commands_router
from .messages import router as messages_router

router = Router(name=__name__)

router.include_routers(commands_router, messages_router)
