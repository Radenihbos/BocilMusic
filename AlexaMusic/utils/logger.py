#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐌𝐞 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐍𝐚𝐌𝐞 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐔𝐬𝐞𝐑𝐧𝐚𝐌𝐞 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐈𝐃  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐂𝐡𝐚𝐭 𝐥𝐢𝐧𝐤: >** {chatusername}
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐒𝐞𝐀𝐫𝐜𝐇𝐞𝐝 𝐅𝐨𝐫:** {message.text}
**━━━━━━━━━━━━━━━**
**⋆ꏠ⋆ 𝐒𝐭𝐫𝐄𝐚𝐦 𝐓𝐲𝐏𝐞:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
