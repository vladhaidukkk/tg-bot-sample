import asyncio
import logging
from re import Match

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

from bot.config import settings

dp = Dispatcher()


@dp.message(
    CommandStart(
        deep_link=True,
        deep_link_encoded=True,
        magic=F.args.regexp(r"^id:(\d+),username:(.+)$").as_("referral"),
    )
)
async def referral_start_command_handler(message: Message, referral: Match[str]) -> None:
    ref_username = referral.group(2)
    await message.answer(text=f"👋 {message.from_user.full_name}. I see @{ref_username} told you about us 🥰")


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(text=f"👋 {message.from_user.full_name}")


@dp.message(Command("ref"))
async def ref_command_handler(message: Message) -> None:
    ref_link = await create_start_link(
        bot=message.bot,
        payload=f"id:{message.from_user.id},username:{message.from_user.username}",
        encode=True,
    )
    await message.answer(text=f"Your referral link: {ref_link}")


@dp.message(Command("help"))
async def help_command_handler(message: Message) -> None:
    await message.answer("I see you need a hero 🦸")


@dp.message(Command("explain", magic=F.args))
async def explain_command_handler(message: Message, command: CommandObject) -> None:
    args = command.args.split(" ")
    for arg in args:
        await message.answer(text=f"Explanation for {arg} 💡")


@dp.message(F.text.regexp(r"^reply:(.+)$").as_("text"))
async def reply_handler(message: Message, text: Match[str]) -> None:
    await message.reply(text=text.group(1))


@dp.message(F.photo)
async def photo_handler(message: Message) -> None:
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id, caption="Thank you for the photo. It looks nice 😁")


@dp.message(F.sticker)
async def sticker_handler(message: Message) -> None:
    sticker_id = message.sticker.file_id
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(text="This sticker is amazing 🤩")


@dp.message(F.animation)
async def animation_handler(message: Message) -> None:
    animation_id = message.animation.file_id
    await message.answer_animation(animation=animation_id, caption="I like this animation 🥰")


@dp.message(F.document)
async def document_handler(message: Message) -> None:
    document_id = message.document.file_id
    await message.answer_document(document=document_id, caption="Thank you for the document. It is interesting 🧐")


@dp.message(F.voice)
async def voice_handler(message: Message) -> None:
    voice_id = message.voice.file_id
    await message.answer_voice(voice=voice_id, caption="Sounds interesting 🤔")


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.copy_to(chat_id=message.chat.id)


async def main() -> None:
    bot = Bot(token=settings.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
