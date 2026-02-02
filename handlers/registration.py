from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.registration import gender_keyboard

router = Router()

@router.callback_query(F.data == "register")
async def start_registration(call: CallbackQuery):
    await call.message.answer(
        "Выберите ваш пол:",
        reply_markup=gender_keyboard()
    )
    await call.answer()