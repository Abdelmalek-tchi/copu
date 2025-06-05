import os
import asyncio
import datetime
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

api_id = 23831415
api_hash = '9f43a4fe515e3838df92c644f55b8b94'
source_channel = "https://t.me/blombardsignal"
target_channel = "https://t.me/cryptsight"

# Setup client
client = TelegramClient("session", api_id, api_hash)

async def forward_recent_messages():
    await client.start()
    now = datetime.datetime.utcnow()
    thirty_minutes_ago = now - datetime.timedelta(minutes=30)

    print(f"⏳ Fetching messages from last 30 minutes in: {source_channel}")
    async for message in client.iter_messages(source_channel, offset_date=thirty_minutes_ago, reverse=True):
        try:
            if message.text or message.media:
                await client.send_message(target_channel, message)
                print(f"✅ Forwarded message ID {message.id}")
        except Exception as e:
            print(f"⚠️ Error forwarding message ID {message.id}: {e}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(forward_recent_messages())
