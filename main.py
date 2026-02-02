import asyncio
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


async def main():
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

    # Стартуем polling
    print("🚀 Бот запущен и готов к работе!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())