from enum import StrEnum

from aiogram.enums.poll_type import PollType
from aiogram.types import KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class MainKeyboardButton(StrEnum):
    INVITE = "🤝 Invite Friend"
    CONTACT = "📞 Share Contact"
    POLL = "📊 Create Poll"
    QUIZ = "🤔 Create Quiz"


def build_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=MainKeyboardButton.INVITE))
    builder.add(KeyboardButton(text=MainKeyboardButton.CONTACT, request_contact=True))
    builder.add(
        KeyboardButton(text=MainKeyboardButton.POLL, request_poll=KeyboardButtonPollType(type=PollType.REGULAR))
    )
    builder.add(KeyboardButton(text=MainKeyboardButton.QUIZ, request_poll=KeyboardButtonPollType(type=PollType.QUIZ)))
    return builder.adjust(2).as_markup(resize_keyboard=True, input_field_placeholder="Click on a button")
