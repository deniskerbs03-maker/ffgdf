import asyncio
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.db import connect_db

# Подключаем все хэндлеры
from handlers import (
    start,
    registration,
    admin_panel,
    antidox,
    chat_settings
)

# ======== Мини-сервер для Render Web Service ========
app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    # Render Web Service требует открытый порт
    app.run(host="0.0.0.0", port=10000)

# ======== Основной бот ========
async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем базу данных
    await connect_db()

    # Подключаем роутеры
    dp.include_router(start.router)
    dp.include_router(registration.router)
    dp.include_router(admin_panel.router)
    dp.include_router(chat_settings.router)
    dp.include_router(antidox.router)

    print("🚀 Бот запущен и готов к работе!")
    await dp.start_polling(bot)

# ======== Запуск Flask и бота параллельно ========
if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(start_bot())