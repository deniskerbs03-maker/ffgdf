from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔍 Поиск чатов", callback_data="search_chats"),
            InlineKeyboardButton(text="💬 Поиск собеседника", callback_data="search_people")
        ],
        [
            InlineKeyboardButton(text="🛠 Поддержка", callback_data="support")
        ]
    ])