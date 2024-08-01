from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router(name=__name__)


class RegistrationState(StatesGroup):
    name = State()
    email = State()
    password = State()


@router.message(Command("reg", "register"))
async def register_command_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationState.name)
    await message.answer("Welcome! What's your name?")


@router.message(RegistrationState.name)
async def registration_name_state_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(RegistrationState.email)
    await message.answer(f"Nice to meet you, {message.text}! What's your email?")


@router.message(RegistrationState.email)
async def registration_email_state_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(email=message.text)
    await state.set_state(RegistrationState.password)
    await message.answer("Great! We are almost done. What's your password?")


@router.message(RegistrationState.password)
async def registration_password_state_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(password=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer("Awesome! You've become a user of our system.")
    await message.answer(
        f"Your credentials:\nUsername: {data['name']}\nEmail: {data['email']}\nPassword length: {len(data['password'])}"
    )
