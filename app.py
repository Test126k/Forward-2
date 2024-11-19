import os
from pyrogram import Client
from pyrogram.errors import FloodWait
import time

api_id = int(os.getenv("26300022"))  # API ID from environment
api_hash = os.getenv("def44e13defba9d104323e821955dfa3")  # API Hash from environment
source_channel = os.getenv("-1002306025697")  # Source channel username or ID
destination_channel = os.getenv("-1002287893610")  # Destination channel username or ID

app = Client("my_forwarder", api_id, api_hash)

with app:
    total_messages = app.get_chat_history_count(source_channel)
    print(f"Total messages to forward: {total_messages}")
    
    for message_id in range(1, total_messages + 1):
        try:
            message = app.get_messages(source_channel, message_id)
            if message:
                app.forward_messages(destination_channel, source_channel, message_id)
                print(f"Forwarded message ID: {message_id}")
        except FloodWait as e:
            print(f"Rate limit hit. Waiting for {e.value} seconds...")
            time.sleep(e.value)
        except Exception as e:
            print(f"Error on message ID {message_id}: {e}")
