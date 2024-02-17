import asyncio

from aiogram.filters import CommandStart, Filter
from aiogram import Bot, types, Dispatcher, F
from aiogram.types.input_file import FSInputFile
from aiogram.filters import CommandStart, Filter
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import CallbackQuery


TOKEN = '6805910622:AAFaoyIFq8QgK8msxdl6mNekSRk1XSoxbCs'

dp = Dispatcher()
bot = Bot(TOKEN)

async def main():
    await dp.start_polling(bot)

def inline_keyboard(text1, text2):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=text1,
        callback_data=MyCallback(foo=text1, bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text=text2,
        callback_data = MyCallback(foo=text2, bar="42")
    )
    return builder.as_markup()

class Command(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.my_text

class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

@dp.message(CommandStart())
async def welcome(message: types.Message):

    await message.answer('Чтобы начать выберите кто вы:', reply_markup=inline_keyboard('Ученик', 'Учитель'))


if __name__ == '__main__':
    print('Bot is running')
    asyncio.run(main())
