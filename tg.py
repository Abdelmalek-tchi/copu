from telethon import TelegramClient, events
import asyncio

# Replace with your own values
api_id = 23831415

api_hash = '9f43a4fe515e3838df92c644f55b8b94'

# Channels
source_channel = 'https://t.me/test00011111112'  # or channel ID
target_channel = 'https://t.me/trading1001off'  # or channel ID

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message = event.message.message
    if message:
        await client.send_message(target_channel, message)

async def main():
    print("Bot is running...")
    await client.start()
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
