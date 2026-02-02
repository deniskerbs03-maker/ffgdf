import asyncio
from threading import Thread
from flask import Flask
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.db import connect_db

# Подключаем все хэндлеры
from handlers import (
    start,             # /start и главное меню
    registration,      # регистрация пользователей
    admin_panel,       # панель создателя
    antidox,           # антидокс с включением/выключением
    chat_settings      # настройки чата (вкл/выкл антидокс)
)

# ======== Мини-сервер для Render Web Service ========
app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    # Render Web Service ожидает открытый порт, используем 10000
    app.run(host="0.0.0.0", port=10000)

# ======== Основной бот ========
async def start_bot():
    # Создаём бот и диспетчер
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
    # Запуск Flask в отдельном потоке
    Thread(target=run_web).start()
    # Запуск бота
    asyncio.run(start_bot())