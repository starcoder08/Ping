from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio

TOKEN = "7904474293:AAGPQZcn57610bNbuV-880IgbUe9e3F6pNQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['ping'])
async def ping_handler(message: types.Message):
    await message.answer("✅ Bot ishlayapti!")

async def ping_bot():
    while True:
        try:
            await bot.send_message("YOUR_CHAT_ID", "/ping")
        except Exception as e:
            print(f"Ping xatolik berdi: {e}")
        await asyncio.sleep(150)  # Har 5 daqiqada ping tashlash

loop = asyncio.get_event_loop()
loop.create_task(ping_bot())  # Ping botni fon jarayonida ishlatish
executor.start_polling(dp, skip_updates=True)