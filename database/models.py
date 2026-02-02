from database.db import get_pool


# ---------- Чаты ----------

async def get_admin_chats(owner_id: int):
    pool = await get_pool()
    return await pool.fetch(
        "SELECT * FROM chats WHERE owner_id = $1",
        owner_id
    )


# ---------- Настройки чатов ----------

async def get_chat_settings(chat_id: int):
    pool = await get_pool()
    return await pool.fetchrow(
        "SELECT * FROM chat_settings WHERE chat_id = $1",
        chat_id
    )


async def create_chat_settings(chat_id: int):
    pool = await get_pool()
    await pool.execute(
        """
        INSERT INTO chat_settings (chat_id)
        VALUES ($1)
        ON CONFLICT (chat_id) DO NOTHING
        """,
        chat_id
    )


async def toggle_antidox(chat_id: int):
    pool = await get_pool()
    await pool.execute(
        """
        UPDATE chat_settings
        SET antidox = NOT antidox
        WHERE chat_id = $1
        """,
        chat_id
    )