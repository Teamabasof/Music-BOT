# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Copyright (C) 2021 By @Itz_VeNom_xD
# Copyright (C) 2021 By @Dr_Asad_Ali
# Copyright (C) 2021 By @HarshitSharma361


from typing import List
from pyrogram.types import Chat, User
import rocks.cache.admins


async def get_administrators(chat: Chat) -> List[User]:
    get = rocks.cache.admins.get(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        rocks.cache.admins.set(chat.id, to_set)
        return await get_administrators(chat)
