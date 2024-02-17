import asyncio

from aiogram.filters import CommandStart, Filter
from aiogram import Bot, types, Dispatcher, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


TOKEN = '6805910622:AAFaoyIFq8QgK8msxdl6mNekSRk1XSoxbCs'

dp = Dispatcher()
bot = Bot(TOKEN)


async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    print('Bot is running')
    asyncio.run(main())

