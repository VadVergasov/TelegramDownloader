import asyncio
import logging

from telethon import TelegramClient, events, sync

import config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

client = TelegramClient("session", config.API_ID, config.API_HASH)


@client.on(events.NewMessage(chats=config.CHAT))
async def handler(event):
    await client.download_media(event.message)


client.start()
client.run_until_disconnected()
