from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from config import SUPERADMIN_ID
from keyboards.admin import admin_main_menu, chat_card
from database.models import get_admin_chats

router = Router()


# --------- Вход в админ-панель ---------

@router.message(commands=["admin"])
async def admin_panel(message: Message):
    if message.from_user.id != SUPERADMIN_ID:
        return

    await message.answer(
        "👑 Панель создателя\n\nВыберите раздел:",
        reply_markup=admin_main_menu()
    )


# --------- Мои чаты ---------

@router.callback_query(F.data == "admin_chats")
async def admin_chats(call: CallbackQuery):
    if call.from_user.id != SUPERADMIN_ID:
        return

    chats = await get_admin_chats(call.from_user.id)

    if not chats:
        await call.message.answer("❌ У вас пока нет подключённых чатов.")
        await call.answer()
        return

    for chat in chats:
        text = (
            f"📍 <b>{chat['title']}</b>\n"
            f"🆔 ID чата: <code>{chat['id']}</code>"
        )

        await call.message.answer(
            text,
            reply_markup=chat_card(chat["id"]),
            parse_mode="HTML"
        )

    await call.answer()


# --------- Назад в главное меню ---------

@router.callback_query(F.data == "admin_back")
async def admin_back(call: CallbackQuery):
    if call.from_user.id != SUPERADMIN_ID:
        return

    await call.message.answer(
        "👑 Панель создателя\n\nВыберите раздел:",
        reply_markup=admin_main_menu()
    )
    await call.answer()