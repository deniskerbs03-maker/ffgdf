from aiogram import Router, F
from aiogram.types import CallbackQuery
from config import SUPERADMIN_ID
from keyboards.chat_settings import chat_settings_keyboard
from database.models import (
    get_chat_settings,
    create_chat_settings,
    toggle_antidox
)

router = Router()


@router.callback_query(F.data.startswith("chat_settings:"))
async def open_chat_settings(call: CallbackQuery):
    if call.from_user.id != SUPERADMIN_ID:
        return

    chat_id = int(call.data.split(":")[1])

    await create_chat_settings(chat_id)
    settings = await get_chat_settings(chat_id)

    await call.message.answer(
        f"⚙ Настройки чата\n🆔 <code>{chat_id}</code>",
        reply_markup=chat_settings_keyboard(chat_id, settings["antidox"]),
        parse_mode="HTML"
    )
    await call.answer()


@router.callback_query(F.data.startswith("toggle_antidox:"))
async def toggle_antidox_handler(call: CallbackQuery):
    if call.from_user.id != SUPERADMIN_ID:
        return

    chat_id = int(call.data.split(":")[1])

    await toggle_antidox(chat_id)
    settings = await get_chat_settings(chat_id)

    await call.message.edit_reply_markup(
        reply_markup=chat_settings_keyboard(chat_id, settings["antidox"])
    )
    await call.answer("Готово")