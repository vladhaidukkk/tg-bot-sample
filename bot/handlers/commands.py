from re import Match

from aiogram import F, Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

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
    await message.answer(text=f"👋 {message.from_user.full_name}. I see @{ref_username} told you about us 🥰")


@router.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(text=f"👋 {message.from_user.full_name}")


@router.message(Command("ref"))
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
