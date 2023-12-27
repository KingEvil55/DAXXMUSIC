from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ",callback_data="settings_back_helper",),
            InlineKeyboardButton(text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="settings_back_helper"),
        ],
        [    
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 1", url=f"https://t.me/Animes_in_hindi_dub",),
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 2", url=f"https://t.me/All_In_Hindi_Dubbed",),
        ],
        [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ 1", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ 2", url=f"https://t.me/AppoloXCommunity",),
        ],   
        [  
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER),
        ],
     ]
    return buttons
