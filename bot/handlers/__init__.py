from aiogram import Router

from .admin import router as admins_router
from .commands import router as commands_router
from .messages import router as messages_router
from .quotes import router as quotes_router
from .registration import router as registration_survey_router

router = Router(name=__name__)

router.include_routers(
    registration_survey_router,
    commands_router,
    admins_router,
    quotes_router,
    messages_router,
)
