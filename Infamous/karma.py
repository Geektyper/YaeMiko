# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/146c9930d2198618dfbba.jpg",
    "https://telegra.ph/file/b32a605a9804bcdf41a83.jpg",
    "https://telegra.ph/file/1db47f3c4379b1959023e.jpg",
    "https://telegra.ph/file/18a457ee327c22eb576b7.jpg",
    "https://telegra.ph/file/f0fcb69934b394fc57c19.jpg",
]

HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ɴᴇᴢᴜᴋᴏ, ᴀ ᴅᴇᴍᴏɴ ꜱʟᴀʏᴇʀ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/Divine_x_soul"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="SUPPORT", url="https://t.me/Divine_x_soul"),
            ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ɴᴇᴢᴜᴋᴏ* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
