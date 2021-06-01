# alfareza

import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "AlphaZ-Plugins",
            api_id=int(os.environ.get("API_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: ")
    ) as userge:
        print("\nprocessing...")
        await alphaz.send_message(
            "me", f"#ALPHAZ-PLUGINS #HU_STRING_SESSION\n\n```{await userge.export_session_string()}```")
        print("Done !, session string has been sent to saved messages!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
