# alfareza

import os

from telegraph import upload_file

from alphaz import alphaz, Message, Config
from alphaz.utils import progress

_T_LIMIT = 5242880


@alphaz.on_cmd("telegraph", about={
    'header': "Unggah file ke server Telegraph",
    'types': ['.jpg', '.jpeg', '.png', '.gif', '.mp4'],
    'usage': "reply {tr}telegraph to supported media : limit 5MB"})
async def telegraph_(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.err("reply untuk didukung media")
        return
    if not ((replied.photo and replied.photo.file_size <= _T_LIMIT)
            or (replied.animation and replied.animation.file_size <= _T_LIMIT)
            or (replied.video and replied.video.file_name.endswith('.mp4')
                and replied.video.file_size <= _T_LIMIT)
            or (replied.document
                and replied.document.file_name.endswith(
                    ('.jpg', '.jpeg', '.png', '.gif', '.mp4'))
                and replied.document.file_size <= _T_LIMIT)):
        await message.err("not supported!")
        return
    await message.edit("`processing...`")
    dl_loc = await message.client.download_media(
        message=message.reply_to_message,
        file_name=Config.DOWN_PATH,
        progress=progress,
        progress_args=(message, "mencoba mengunduh")
    )
    await message.edit("`mengunggah ke telegraph...`")
    try:
        response = upload_file(dl_loc)
    except Exception as t_e:
        await message.err(t_e)
    else:
        await message.edit(f"**[Telegraph Link By AlphaZ Plugins](https://telegra.ph{response[0]})**")
    finally:
        os.remove(dl_loc)
