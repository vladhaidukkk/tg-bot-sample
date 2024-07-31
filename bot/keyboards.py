from enum import StrEnum

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class MainKeyboardButton(StrEnum):
    INVITE = "🤝 Invite Friend"


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=MainKeyboardButton.INVITE)]],
    resize_keyboard=True,
    input_field_placeholder="Click on a command",
)
