import asyncio

from aiogram.filters import CommandStart, Filter
from aiogram import Bot, types, Dispatcher, F
from aiogram.types.input_file import FSInputFile
from aiogram.filters import CommandStart, Filter
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackQuery


TOKEN = '6805910622:AAFaoyIFq8QgK8msxdl6mNekSRk1XSoxbCs'

dp = Dispatcher()
bot = Bot(TOKEN)

#Flags:
who = ''

async def main():
    await dp.start_polling(bot)

class Command(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: types.Message) -> bool:
        return message.text == self.my_text


@dp.message(CommandStart())
async def welcome(message: types.Message, text1='Ученик', text2='Учитель'):
    global who
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=text1,
        callback_data="Ученик")
    )

    builder.add(types.InlineKeyboardButton(
        text=text2,
        callback_data="Учитель")
    )


    await message.answer(
        "Чтобы начать выберите кто вы:",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == 'Ученик')
async def student_welcome_msg(callback: types.CallbackQuery):
    who = 'Ученик'
    await callback.message.answer(f'Вы {who}')

@dp.callback_query(F.data == 'Учитель')
async def student_welcome_msg(callback: types.CallbackQuery):
    who = 'Учитель'
    await callback.message.answer(f'Вы {who}')


if __name__ == '__main__':
    print('Bot is running')
    asyncio.run(main())
