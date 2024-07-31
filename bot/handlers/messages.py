from re import Match

from aiogram import F, Router
from aiogram.types import Message

router = Router(name=__name__)


@router.message(F.text.regexp(r"^reply:(.+)$").as_("text"))
async def reply_handler(message: Message, text: Match[str]) -> None:
    await message.reply(text=text.group(1))


@router.message(F.photo)
async def photo_handler(message: Message) -> None:
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id, caption="Thank you for the photo. It looks nice 😁")


@router.message(F.sticker)
async def sticker_handler(message: Message) -> None:
    sticker_id = message.sticker.file_id
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(text="This sticker is amazing 🤩")


@router.message(F.animation)
async def animation_handler(message: Message) -> None:
    animation_id = message.animation.file_id
    await message.answer_animation(animation=animation_id, caption="I like this animation 🥰")


@router.message(F.document)
async def document_handler(message: Message) -> None:
    document_id = message.document.file_id
    await message.answer_document(document=document_id, caption="Thank you for the document. It is interesting 🧐")


@router.message(F.voice)
async def voice_handler(message: Message) -> None:
    voice_id = message.voice.file_id
    await message.answer_voice(voice=voice_id, caption="Sounds interesting 🤔")


@router.message()
async def echo_handler(message: Message) -> None:
    await message.copy_to(chat_id=message.chat.id)
