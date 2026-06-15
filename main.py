import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Performance VPN\n\n"
        "🚀 Добро пожаловать\n"
        "📦 Тарифы\n👤 Профиль\n💬 Поддержка"
    )

async def main():
    print("bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())