# (c) @LazyDeveloperr

from configs import Config
from handlers.database import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\n🇳 🇪 🇼  🇺 🇸 🇪 🇷 [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n#User_id: {cmd.from_user.id}\n🇨 🇴 🇳 🇳 🇪 🇨 🇹 🇪 🇩  🇹 🇴 @{Config.BOT_USERNAME} !!"
            )
            
