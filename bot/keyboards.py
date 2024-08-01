from enum import StrEnum

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class MainKeyboardButton(StrEnum):
    INVITE = "🤝 Invite Friend"
    CONTACT = "📞 Share Contact"


def build_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=MainKeyboardButton.INVITE))
    builder.add(KeyboardButton(text=MainKeyboardButton.CONTACT, request_contact=True))
    return builder.adjust(2).as_markup(resize_keyboard=True, input_field_placeholder="Click on a button")
