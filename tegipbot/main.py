from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
import aiohttp
import asyncio
import logging
import os


logging.basicConfig(filename="bot.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or "YOUR_BOT_TOKEN"
bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def start(message: Message) -> None:
    try:
        
        await bot.send_message(message.chat.id, "Welcome! Send me an IP address or domain name to get its location. (IPV4 or IPV6)")
        return 
    
    except Exception as e:
        logging.error(f"Error in start command: {e}")
        return
    
    
@bot.message_handler(func=lambda m: True)
async def parse_json(message: Message) -> dict:
    try:
        
        query = message.text
        url = f"http://ip-api.com/json/{query if query != "" else ""}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                await send_location(message, data)
                return data
    
    except Exception as e:
        logging.error(f"Error fetching IP data: {e}")
        return {"status": "fail"}

async def send_location(message: Message, data: dict):
    try:
        
        if data['status'] == 'fail':
            await bot.reply_to(message, "Invalid IP address or domain name.")
            return
        else:
            location = f"IP: {data['query']}\n" \
                    f"Country: {data['country']}\n" \
                    f"Region: {data['regionName']}\n" \
                    f"City: {data['city']}\n" \
                    f"ISP: {data['isp']}\n" \
                    f"Latitude: {data['lat']}\n" \
                    f"Longitude: {data['lon']}"
                    
            location += f"\nGoogle Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}"
            await bot.reply_to(message, location)
            return
            
    except Exception as e:
        logging.error(f"Error sending location: {e}")
        await bot.reply_to(message, "An error occurred while processing your request.")
        return
        
if __name__ == "__main__":
    try:
        logging.info("Bot is running")
        asyncio.run(bot.polling(none_stop=True))
    except Exception as e:
        logging.error(f"Error: {e}")