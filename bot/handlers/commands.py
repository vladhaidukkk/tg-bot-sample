from re import Match

from aiogram import F, Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from aiogram.utils.deep_linking import create_start_link, create_telegram_link

from bot.keyboards import MainKeyboardButton, build_main_keyboard

router = Router(name=__name__)


@router.message(
    CommandStart(
        deep_link=True,
        deep_link_encoded=True,
        magic=F.args.regexp(r"^id:(\d+),username:(.+)$").as_("referral"),
    )
)
async def referral_start_command_handler(message: Message, referral: Match[str]) -> None:
    ref_username = referral.group(2)
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👀 Go to Your Friend", url=create_telegram_link(ref_username)),
                InlineKeyboardButton(text="🚀 Begin Your Journey", callback_data="begin"),
            ],
            [InlineKeyboardButton(text="📺 Open YouTube", web_app=WebAppInfo(url="https://youtube.com"))],
        ]
    )
    await message.answer(
        text=f"👋 {message.from_user.full_name}. I see @{ref_username} told you about us 🥰",
        reply_markup=inline_keyboard,
    )


@router.callback_query(F.data == "begin")
async def begin_journey_handler(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    await callback_query.message.answer(text="🌄 Let's begin our journey", reply_markup=build_main_keyboard())


@router.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(text=f"👋 {message.from_user.full_name}", reply_markup=build_main_keyboard())


@router.message(Command("ref"))
@router.message(F.text == MainKeyboardButton.INVITE)
async def ref_command_handler(message: Message) -> None:
    ref_link = await create_start_link(
        bot=message.bot,
        payload=f"id:{message.from_user.id},username:{message.from_user.username}",
        encode=True,
    )
    await message.answer(text=f"Your referral link: {ref_link}")


@router.message(Command("help"))
async def help_command_handler(message: Message) -> None:
    await message.answer("I see you need a hero 🦸")


@router.message(Command("explain", magic=F.args))
async def explain_command_handler(message: Message, command: CommandObject) -> None:
    args = command.args.split(" ")
    for arg in args:
        await message.answer(text=f"Explanation for {arg} 💡")
