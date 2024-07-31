from enum import StrEnum

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class MainKeyboardButton(StrEnum):
    INVITE = "🤝 Invite Friend"
    CONTACT = "📞 Share Contact"


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=MainKeyboardButton.INVITE)],
        [KeyboardButton(text=MainKeyboardButton.CONTACT, request_contact=True)],
    ],
    resize_keyboard=True,
    input_field_placeholder="Click on a button",
)
