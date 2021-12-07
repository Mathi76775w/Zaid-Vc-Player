import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f323bcaec71ba138fb6df.png",
        caption=f"""**A Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Bᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Pʟᴀʏ Mᴜsɪᴄ Oɴ Gʀᴏᴜᴘs Tʜʀᴏᴜɢʜ Tʜᴇ Nᴇᴡ Tᴇʟᴇɢʀᴀᴍ's Vᴏɪᴄᴇ Cʜᴀᴛs Pᴏᴡᴇʀ Bʏ⚡[PʏTɢCᴀʟʟs](t.me/!.
 Aᴅᴅ Mᴇ Tᴏ Uʀ Cʜᴀᴛ Fᴏʀ Aɴᴅ Hᴇʟᴘ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cʟɪᴄᴋ Oɴ Bᴜᴛᴛᴏɴs  ...
💞  These Features A.I Based 
Mᴀᴅᴇ Wɪᴛʜ 🖤 Bʏ [𝗩𝗶𝗷𝗮𝘆](t.me/Attitude_king_vj) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐔𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url=f"https://t.me/tgcalls_Music_update/13"
                    ),
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/Attitude_king_vj"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 😈", url=f"https://t.me/{ZAID_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6882544289d57512d143d.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["Ntg", "Do"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/92688f2c44a35ba673c23.png",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/itsunknown-12/Zaid-Vc-Player")
                ]
            ]
        ),
    )
