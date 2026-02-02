from aiogram import Router
from aiogram.types import Message
from keyboards.main_menu import main_menu
from database.models import create_user

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await create_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )

    text = (
        "👋 Привет!\n\n"
        "Я — бот для модерации чатов и поиска собеседников между сообществами.\n\n"
        "Выберите действие 👇"
    )

    await message.answer(text, reply_markup=main_menu())