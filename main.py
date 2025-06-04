from telethon import TelegramClient, events
import asyncio
import time
import os
from keep_alive import keep_alive
keep_alive()

# Your API ID and Hash from my.telegram.org
api_id = os.environ.get('apid')
api_hash = os.environ.get('aphash')

# Your phone number
phone = '+998902920550'

# The target bot username
target_bot = 'mini4oyinlar_bot'

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    
    await client.start(phone)
    print("Client Created")
    
    # Ensure you're authorized
    if not await client.is_user_authorized():
        print("Not authorized!")
        return
    
    while True:
        try:
            # Send /top command to the bot
            await client.send_message(target_bot, '/top')
            print(f"Sent /top to {target_bot} at {time.strftime('%X')}")
            
            # Wait for 5 minutes (300 seconds)
            await asyncio.sleep(300)
            
        except Exception as e:
            print(f"Error occurred: {e}")
            # Wait for 1 minute before retrying
            await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
