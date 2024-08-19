# (c) @LazyDeveloperr

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=iTS_ViSHWA14_{str_to_b64(str(SaveMessage.id))}"
        await editable.edit(
            f"**Bᴀᴛᴄʜ Fɪʟᴇꜱ Sᴛᴏʀᴇᴅ Iɴ Mʏ Dᴀᴛᴀʙᴀꜱᴇ!**\n\nHᴇʀᴇ ɪꜱ ᴛʜᴇ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴏғ ʏᴏᴜʀ ғɪʟᴇꜱ: {share_link} \n\n"
            f"Jᴜꜱᴛ Cʟɪᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇꜱ!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Oᴘᴇɴ Lɪɴᴋ🔗", url=share_link)],
                 [InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ💥", url="https://t.me/Marathi_Tv_Serials"),
                  InlineKeyboardButton("Oᴡɴᴇʀ😎", url="https://t.me/iTS_ViSHWA14")]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Link", url=share_link)]])
        )
        # ✧ Bina soche smjhe code edit mt krna wrna error dhundne mei umrr beet jaayega.
        # ✧ source code upgraded by The sir LazyDeveloper 
        # ✧ Don't remove credit ✧ @LazyDeveloper ✧
        if(Config.LAZY_MODE == True):
            thumbs= message.video.thumbs[0]
            file_id= thumbs.file_id
            lazy_channel = int(Config.LAZY_CHANNEL)
            location=await bot.download_media(file_id)
            lazypost_channel_username = (Config.LP_CHANNEL_USRNM)
            lazypost_ch_admin_usrnm = (Config.LPCH_ADMIN_USRMN)
            main_channel_username = (Config.LP_BTN_MAIN_CH_USRNM)
            main_btn_link = f"https://telegram.me/{main_channel_username}"
            file_name = message.caption
            caption_z = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_za = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_zab = f"{file_name}\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_zabi = f"{file_name}\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            lazy_dev = f"+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            lazypost_custom_template = f"{(Config.LP_CUSTOM_TEMPLATE)}\n\n{lazy_dev} ♥️"
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⎝⎝✧ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ✧⎠⎠", url=share_link)],
                 [InlineKeyboardButton("⚡️✧ ɢᴇᴛ ʙᴀᴛᴄʜ ꜰɪʟᴇꜱ ✧⚡️", url=share_link)],
                ]
            )
            main_btn=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⎝⎝✧ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ✧⎠⎠", url=share_link)],
                 [InlineKeyboardButton("⚡️✧ ɢᴇᴛ ʙᴀᴛᴄʜ ꜰɪʟᴇꜱ ✧⚡️", url=share_link)],
                 [InlineKeyboardButton("•⊹Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⊹•", url=main_btn_link)]
                ]
            )
            # ✧ Here is the condition for sending POST in movie channel
            if(Config.LP_CUSTOM_TEMPLATE):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=reply_markup)
            elif(Config.LP_CUSTOM_TEMPLATE and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=reply_markup)
            elif(Config.LP_CHANNEL_USRNM and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=reply_markup)
            elif(Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=main_btn)
            elif(Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=reply_markup)
            else:
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zabi,reply_markup=reply_markup)
                # ✧ Please don't add unnescesary things here >[LazyDeveloper]
                cptz = f"🥷\n\nღ♡ **𝘗𝘖𝘚𝘛 𝘜𝘗𝘓𝘖𝘈𝘋𝘌𝘋 𝘖𝘕 𝘊𝘏𝘈𝘕𝘕𝘌𝘓 𝘚𝘜𝘊𝘊𝘌𝘚𝘚𝘍𝘜𝘓𝘓𝘠**✅\n\n**• NOTE: **ᴘʟᴇᴀꜱᴇ ᴏɴʟʏ ᴄʟɪᴄᴋ ->** ɢᴇᴛ ʙᴀᴛᴄʜ & ᴘᴏꜱᴛ **<- ᴏɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴍᴇꜱꜱᴀɢᴇꜱ\n\nN͢O͢ o͢f͢ c͢l͢i͢c͢k͢ = n͢o͢ o͢f͢ p͢o͢s͢t͢s͢\n\n• ʙᴇ ᴄᴀʀᴇꜰᴜʟʟ - ʏᴏᴜ ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ɪɴ ʟᴀᴢʏ_ᴍᴏᴅᴇ\n• @ʟᴀᴢʏᴅᴠᴇʟᴏᴘᴇʀ"
                k = await message.reply_text(text=cptz)
                await asyncio.sleep(30)
                await k.delete()
        
    except Exception as err:
        await editable.edit(f"ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ...\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )

async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            disable_web_page_preview=True)
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=LazyDeveloperr_{str_to_b64(file_er_id)}"
        await editable.edit(
            "**Yᴏᴜʀ Fɪʟᴇꜱ Sᴛᴏʀᴇᴅ Iɴ MY Dᴀᴛᴀʙᴀꜱᴇ!**\n\n"
            f"Hᴇʀᴇ ɪꜱ ᴛʜᴇ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴏғ ʏᴏᴜʀ ғɪʟᴇꜱ: {share_link}  \n\n"
            f"Jᴜꜱᴛ Cʟɪᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇꜱ..!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⚡️ Open Link ⚡️", url=share_link)],
                 [InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ💥", url="https://t.me/Marathi_Tv_Serials"),
                  InlineKeyboardButton("Oᴡɴᴇʀ😎", url="https://t.me/iTS_ViSHWA14")]]
            ),
            disable_web_page_preview=True
        )
        # ✧ Bina soche smjhe code edit mt krna wrna error dhundne mei umrr beet jaayega.
        # ✧ source code upgraded by The sir LazyDeveloper 
        # ✧ Don't remove credit ✧ @LazyDeveloper ✧
        if(Config.LAZY_MODE == True):
            thumbs= message.video.thumbs[0]
            file_id= thumbs.file_id
            lazy_channel = int(Config.LAZY_CHANNEL)
            location=await bot.download_media(file_id)
            lazypost_channel_username = (Config.LP_CHANNEL_USRNM)
            lazypost_ch_admin_usrnm = (Config.LPCH_ADMIN_USRMN)
            main_channel_username = (Config.LP_BTN_MAIN_CH_USRNM)
            main_btn_link = f"https://telegram.me/{main_channel_username}"
            file_name = message.caption
            caption_z = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_za = f"{file_name}\n\n༺ᴊᴏɪɴ @{lazypost_channel_username} ༻\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_zab = f"{file_name}\n\n🦋・‥☆𝘼𝘿𝙈𝙞𝙉 𝙨𝙪𝙥𝙥𝙤𝙧𝙩☆‥・🦋\n╰┈➤・☆ @{lazypost_ch_admin_usrnm} \n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            caption_zabi = f"{file_name}\n\n+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            lazy_dev = f"+> ᴛʜᴀɴᴋ ʏᴏᴜ <a href='https://telegram.me/iTS_ViSHWA14'>╰☆☆ 𝒱𝒾𝒮𝐻𝒲𝒜 ☆☆╮</a>"
            lazypost_custom_template = f"{(Config.LP_CUSTOM_TEMPLATE)}\n\n{lazy_dev} ♥️"
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⎝⎝✧ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ✧⎠⎠", url=share_link)],
                 [InlineKeyboardButton("★ Gᴇᴛ Fɪʟᴇ ★", url=share_link)],
                ]
            )
            main_btn=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⎝⎝✧ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ✧⎠⎠", url=share_link)],
                 [InlineKeyboardButton("★ Gᴇᴛ Fɪʟᴇ ★", url=share_link)],
                 [InlineKeyboardButton("•⊹Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⊹•", url=main_btn_link)]
                ]
            )
            # ✧ Here is the condition for sending POST in movie channel ✧ LazyDeveloper ✧
            if(Config.LP_CUSTOM_TEMPLATE):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=reply_markup)
            elif(Config.LP_CUSTOM_TEMPLATE and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=lazypost_custom_template,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM and Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_z,reply_markup=reply_markup)
            elif(Config.LP_CHANNEL_USRNM and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=main_btn)
            elif(Config.LP_CHANNEL_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_za,reply_markup=reply_markup)
            elif(Config.LPCH_ADMIN_USRMN and Config.LP_BTN_MAIN_CH_USRNM):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=main_btn)
            elif(Config.LPCH_ADMIN_USRMN):
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zab,reply_markup=reply_markup)
            else:
                # ✧ Please don't add unnescesary things here >[LazyDeveloper]
                await bot.send_photo(lazy_channel,photo=location,caption=caption_zabi,reply_markup=reply_markup)
                cptz = f"🥷\n\nღ♡ **𝘗𝘖𝘚𝘛 𝘜𝘗𝘓𝘖𝘈𝘋𝘌𝘋 𝘖𝘕 𝘊𝘏𝘈𝘕𝘕𝘌𝘓 𝘚𝘜𝘊𝘊𝘌𝘚𝘚𝘍𝘜𝘓𝘓𝘠**✅\n\n• ʙᴇ ᴄᴀʀᴇꜰᴜʟʟ - ʏᴏᴜ ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ɪɴ ʟᴀᴢʏ_ᴍᴏᴅᴇ\n• @iTS_ViSHWA14"
                k = await message.reply_text(text=cptz)
                await asyncio.sleep(40)
                await k.delete()

    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ...\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
