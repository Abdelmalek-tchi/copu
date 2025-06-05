# main.py

import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient


API_ID = 23831415
API_HASH = '9f43a4fe515e3838df92c644f55b8b94'
SESSION_NAME = "session"
SOURCE_CHANNEL = "https://t.me/blombardsignal"
TARGET_CHANNEL = "https://t.me/cryptsight"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def forward_recent_messages():
    await client.start()
    print("Client started.")

    now = datetime.utcnow()
    cutoff = now - timedelta(minutes=30)

    async for message in client.iter_messages(SOURCE_CHANNEL, reverse=True, offset_date=cutoff):
        try:
            await client.forward_messages(TARGET_CHANNEL, message)
            print(f"Forwarded: {message.id}")
        except Exception as e:
            print(f"Failed to forward message {message.id}: {e}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(forward_recent_messages())
