import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPERADMIN_ID = int(os.getenv("SUPERADMIN_ID"))

# Для Render или локальной работы с БД
DATABASE_URL = os.getenv("DATABASE_URL")