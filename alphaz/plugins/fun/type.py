# alfareza

import time
import random

from pyrogram.errors.exceptions import FloodWait

from alphaz import userge, Message


@alphaz.on_cmd("type", about={
    'header': "Simulate a typewriter",
    'usage': "{tr}type [text]"})
async def type_(message: Message):
    text = message.input_str
    if not text:
        await message.err("input not found")
        return
    s_time = 0.1
    typing_symbol = '|'
    old_text = ''
    await message.edit(typing_symbol)
    time.sleep(s_time)
    for character in text:
        s_t = s_time / random.randint(1, 100)
        old_text += character
        typing_text = old_text + typing_symbol
        try:
            await message.try_to_edit(typing_text, sudo=False)
            time.sleep(s_t)
            await message.try_to_edit(old_text, sudo=False)
            time.sleep(s_t)
        except FloodWait as x_e:
            time.sleep(x_e.x)
