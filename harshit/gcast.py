# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Copyright (C) 2021 By @Itz_VeNom_xD
# Copyright (C) 2021 By @Dr_Asad_Ali
# Copyright (C) 2021 By @HarshitSharma361

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from rocks.clientbot.clientbot import client as asad
from rocks.config import SUDO_USERS


@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent = 0
    failed = 0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Stɑɤtɩŋʛ Ɓɤøɑɗƈɑst ...`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in asad.iter_dialogs():
            try:
                await asad.send_message(dialog.chat.id, lmao)
                sent = sent + 1
                await wtf.edit(
                    f"`Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats"
                )
                await asyncio.sleep(3)
            except:
                failed = failed + 1
        await message.reply_text(
            f"`Ɠƈɑst Sʋƈƈɘssfʋɭɭy` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} Ƈɦɑts"
        )
