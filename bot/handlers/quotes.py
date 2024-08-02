from contextlib import suppress
from typing import Literal

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router(name=__name__)


quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs 💼❤️",
    "In the end, we only regret the chances we didn't take. – Lewis Carroll 🚀🌟",
    "Life is what happens when you're busy making other plans. – John Lennon 🎶🌍",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill 🏆💪",
    "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama 😊✨",
]


class QuotesCallbackData(CallbackData, prefix="quotes"):
    action: Literal["prev", "current", "next"]
    page: int


def build_quotes_pagination_kb(current_page: int) -> InlineKeyboardMarkup:
    min_page = 0
    max_page = len(quotes) - 1

    prev_page = current_page - 1 if current_page > min_page else min_page
    next_page = current_page + 1 if current_page < max_page else max_page

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="prev", callback_data=QuotesCallbackData(action="prev", page=prev_page).pack()
                ),
                InlineKeyboardButton(
                    text=f"{current_page}", callback_data=QuotesCallbackData(action="current", page=current_page).pack()
                ),
                InlineKeyboardButton(
                    text="next", callback_data=QuotesCallbackData(action="next", page=next_page).pack()
                ),
            ]
        ]
    )


@router.message(Command("quotes"))
async def show_quotes_handler(message: Message) -> None:
    page = 0
    await message.answer(text=quotes[page], reply_markup=build_quotes_pagination_kb(current_page=page))


@router.callback_query(QuotesCallbackData.filter(F.action.in_({"prev", "next"})))
async def show_prev_quote_handler(query: CallbackQuery, callback_data: QuotesCallbackData) -> None:
    with suppress(TelegramBadRequest):
        await query.message.edit_text(
            text=quotes[callback_data.page], reply_markup=build_quotes_pagination_kb(current_page=callback_data.page)
        )
    await query.answer()


@router.callback_query(QuotesCallbackData.filter(F.action == "current"))
async def show_current_quote_handler(query: CallbackQuery) -> None:
    await query.answer()
