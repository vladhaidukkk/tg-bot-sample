from aiogram import Router

from .commands import router as commands_router
from .messages import router as messages_router
from .registration import router as registration_survey_router

router = Router(name=__name__)

router.include_routers(
    registration_survey_router,
    commands_router,
    messages_router,
)
