import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷—————————"
    elif 10 < anon < 20:
        bar = "—𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷————————"
    elif 20 <= anon < 30:
        bar = "——𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷———————"
    elif 30 <= anon < 40:
        bar = "———𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷——————"
    elif 40 <= anon < 50:
        bar = "————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷—————"
    elif 50 <= anon < 60:
        bar = "—————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷————"
    elif 60 <= anon < 70:
        bar = "——————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷———"
    elif 70 <= anon < 80:
        bar = "———————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷——"
    elif 80 <= anon < 95:
        bar = "————————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷—"
    else:
        bar = "—————————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="resume⏭",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="pause⏸", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ᴜʀ ᴘʟᴀʏʟɪsᴛ", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="skip⏮", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="stop.⏹", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷—————————"
    elif 10 < anon < 20:
        bar = "—𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷————————"
    elif 20 <= anon < 30:
        bar = "——💗🤝———————"
    elif 30 <= anon < 40:
        bar = "———⏯️🎵——————"
    elif 40 <= anon < 50:
        bar = "————chal rha hu—————"
    elif 50 <= anon < 60:
        bar = "—————🤪💗🤝————"
    elif 60 <= anon < 70:
        bar = "——————baby💗🤪———"
    elif 70 <= anon < 80:
        bar = "———————𝙸𝚖𝙽𝚘𝚝🫣𝙰𝚟𝙰𝚗𝙸𝚜𝙷——"
    elif 80 <= anon < 95:
        bar = "————————mai hu Avanish🤪—"
    else:
        bar = "—————————khatam ab new lga song"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="Resume⏭",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="pause⏸", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="skip⏮", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="stop⏹", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="Resume⏭",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="pause⏸", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ᴜʀ ᴘʟᴀʏʟɪsᴛ", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="skip⏮", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="stop⏹", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="Resume⏭",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="pause⏸", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="skip⏮", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="stop⏹", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="resume⏭",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="skip⏮",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏꜱᴇ", callback_data="close"
                    ),
                    InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="resume⏭",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="stop⏸", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ᴜʀ ᴘʟᴀʏʟɪsᴛ", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="skip⏮", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="stop⏹", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/imnot_avanish"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏꜱᴇ", callback_data=f"close"
            )
        ],
    ]
    return buttons
    
