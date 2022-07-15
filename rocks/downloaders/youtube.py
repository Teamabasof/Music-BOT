# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Copyright (C) 2021 By @Itz_VeNom_xD
# Copyright (C) 2021 By @Dr_Asad_Ali
# Copyright (C) 2021 By @HarshitSharma361


from os import path

from yt_dlp import YoutubeDL

from rocks.config import DURATION_LIMIT
from rocks.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {duration} minute(s)",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {duration} minute(s)",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
