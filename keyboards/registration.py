from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def gender_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="👨 Мужской", callback_data="gender_male"),
            InlineKeyboardButton(text="👩 Женский", callback_data="gender_female")
        ],
        [
            InlineKeyboardButton(text="🧩 Другое", callback_data="gender_other")
        ]
    ])