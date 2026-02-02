from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📌 Мои чаты", callback_data="admin_chats")],
        [InlineKeyboardButton(text="📊 Общая статистика", callback_data="admin_stats")],
        [InlineKeyboardButton(text="💬 Поддержка", callback_data="admin_support")]
    ])


def chat_card(chat_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⚙ Настройки чата",
                callback_data=f"chat_settings:{chat_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅ Назад",
                callback_data="admin_back"
            )
        ]
    ])