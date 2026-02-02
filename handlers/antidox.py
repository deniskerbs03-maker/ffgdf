from aiogram import Router
from aiogram.types import Message
from utils.antidox import check_dox
from database.models import get_chat_settings

router = Router()


@router.message()
async def antidox_handler(message: Message):
    if not message.text or message.chat.type == "private":
        return

    settings = await get_chat_settings(message.chat.id)
    if not settings or not settings["antidox"]:
        return

    result = check_dox(message.text)
    if not result:
        return

    try:
        await message.delete()
    except:
        pass

    await message.answer(
        f"🚨 <b>Антидокс</b>\n"
        f"Тип: {result}\n"
        f"👤 @{message.from_user.username or 'без юзернейма'}",
        parse_mode="HTML"
    )