from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

from constants import *
from keyboards import *

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
import os

# pip install aiogram
# pip install python-dotenv

bot = Bot(os.getenv("TOKEN_TG"))
dp = Dispatcher(bot)


async def on_startup(_):
    print("I have been started up")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(greeting, reply_markup=kb_start)


@dp.message_handler(Text(equals="Книги"))
async def books_command(message: types.Message):
    await message.answer(books, reply_markup=kb_books)
    await message.answer(attention)


@dp.message_handler(Text(equals=alg))
async def send_ald_book_command(message: types.document):
    await bot.send_document(message.chat.id, alg_book)


@dp.message_handler(Text(equals=geom))
async def send_geom_book_command(message: types.Message):
    await bot.send_document(message.chat.id, geom_book)


@dp.message_handler(Text(equals=phys))
async def send_phys_book_command(message: types.Message):
    await bot.send_document(message.chat.id, phys_book)


@dp.message_handler(Text(equals=ukr_lang))
async def send_ukr_lang_book_command(message: types.Message):
    await bot.send_document(message.chat.id, ukr_lang_book)


@dp.message_handler(Text(equals=ukr_lit))
async def send_ukr_lit_book_command(message: types.Message):
    await bot.send_document(message.chat.id, ukr_lit_book)


@dp.message_handler(Text(equals=world_lit))
async def send_world_lit_book_command(message: types.Message):
    await bot.send_document(message.chat.id, world_lit_book)


@dp.message_handler(Text(equals=biol))
async def send_biol_book_command(message: types.Message):
    await bot.send_document(message.chat.id, biol_book)


@dp.message_handler(Text(equals=chem))
async def send_chem_book_command(message: types.Message):
    await bot.send_document(message.chat.id, chem_book, caption="Це повне лайно")


@dp.message_handler(Text(equals=geo))
async def send_geo_book_command(message: types.Message):
    await bot.send_document(message.chat.id, geo_book)


@dp.message_handler(Text(equals=world_hist))
async def send_world_hist_book_command(message: types.Message):
    await bot.send_document(message.chat.id, world_hist_book)


@dp.message_handler(Text(equals=ukr_hist))
async def send_ukr_hist_book_command(message: types.Message):
    await bot.send_document(message.chat.id, ukr_hist_book)


@dp.message_handler(Text(equals=it))
async def send_it_book_command(message: types.Message):
    await bot.send_document(message.chat.id, it_book)


@dp.message_handler(Text(equals=exit))
async def exit_keyboard(message: types.Message):
    await message.answer("Головне меню", reply_markup=kb_start)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
