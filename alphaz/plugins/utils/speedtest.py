# alfareza

import os
import wget
import speedtest
from alphaz import userge, Message
from alphaz.utils import humanbytes

CHANNEL = alphaz.getCLogger(__name__)


@alphaz.on_cmd("speedtest", about={'header': "test your server speed"})
async def speedtst(message: Message):
    await message.edit("`Running speed test . . .`")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        await message.try_to_edit("`Performing download test . . .`")
        test.download()
        await message.try_to_edit("`Performing upload test . . .`")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await message.err(text=e)
        return
    path = wget.download(result['share'])
    output = f"""**--Started at {result['timestamp']}--

Client:

ISP: `{result['client']['isp']}`
Country: `{result['client']['country']}`

Server:

Name: `{result['server']['name']}`
Country: `{result['server']['country']}, {result['server']['cc']}`
Sponsor: `{result['server']['sponsor']}`
Latency: `{result['server']['latency']}`

Ping: `{result['ping']}`
Sent: `{humanbytes(result['bytes_sent'])}`
Received: `{humanbytes(result['bytes_received'])}`
Download: `{humanbytes(result['download'] / 8)}/s`
Upload: `{humanbytes(result['upload'] / 8)}/s`**"""
    msg = await message.client.send_photo(chat_id=message.chat.id,
                                          photo=path,
                                          caption=output)
    await CHANNEL.fwd_msg(msg)
    os.remove(path)
    await message.delete()
