import os
import time
import datetime
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

SOURCE_CHAT_ID = "https://t.me/blombardsignal"
TARGET_CHAT_ID = "https://t.me/cryptsight"
bot = Bot(token="8005462987:AAG6O8mt4XWI6C4BRNshCz90svamf-RQ-6Y")

def forward_recent_messages():
    now = int(time.time())
    thirty_minutes_ago = now - 30 * 60

    updates = bot.get_updates()
    for update in updates:
        if update.message and update.message.chat.id == SOURCE_CHAT_ID:
            message = update.message
            message_time = int(message.date.timestamp())

            if message_time >= thirty_minutes_ago:
                try:
                    bot.copy_message(chat_id=TARGET_CHAT_ID, from_chat_id=SOURCE_CHAT_ID, message_id=message.message_id)
                    print(f"✅ Copied message {message.message_id}")
                except TelegramError as e:
                    print(f"⚠️ Error copying message: {e}")

if __name__ == "__main__":
    forward_recent_messages()
