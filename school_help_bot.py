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


@dp.message_handler(Text(equals="Розклад"))
async def schedule_command(message: types.Message):
    await message.answer(schedule_text, reply_markup=kb_schedule)


@dp.message_handler(Text(equals="Розклад дзвінків"))
async def timetable_button(message: types.Message):
    await message.answer(timetable_text, reply_markup=kb_timetable)

@dp.message_handler(Text(equals="1 урок"))
async def lesson1_command(message: types.Message):
    await message.answer(lesson_1, parse_mode="html")


@dp.message_handler(Text(equals="2 урок"))
async def lesson2_command(message: types.Message):
    await message.answer(lesson_2, parse_mode="html")


@dp.message_handler(Text(equals="3 урок"))
async def lesson3_command(message: types.Message):
    await message.answer(lesson_3, parse_mode="html")


@dp.message_handler(Text(equals="4 урок"))
async def lesson4_command(message: types.Message):
    await message.answer(lesson_4, parse_mode="html")


@dp.message_handler(Text(equals="5 урок"))
async def lesson5_command(message: types.Message):
    await message.answer(lesson_5, parse_mode="html")


@dp.message_handler(Text(equals="6 урок"))
async def lesson6_command(message: types.Message):
    await message.answer(lesson_6, parse_mode="html")


@dp.message_handler(Text(equals="7 урок"))
async def lesson7_command(message: types.Message):
    await message.answer(lesson_7, parse_mode="html")


@dp.message_handler(Text(equals="Всі уроки"))
async def all_lesson_command(message: types.Message):
    await message.answer(time_table, parse_mode="Html")


@dp.message_handler(Text(equals="Розклад уроків"))
async def lessons_schedule(message: types.Message):
    await message.answer(lessons_orders_text, reply_markup=kb_lessons_schedule)


@dp.message_handler(Text(equals=monday))
async def monday_schedule(message: types.Message):
    await message.answer(monday_sub, parse_mode="Html")


@dp.message_handler(Text(equals=tuesday))
async def tuesday_schedule(message: types.Message):
    await message.answer(tuesday_sub, parse_mode="Html")


@dp.message_handler(Text(equals=wednesday))
async def wednesday_schedule(message: types.Message):
    await message.answer(wednesday_sub, parse_mode="Html")


@dp.message_handler(Text(equals=thursday))
async def thursday_schedule(message: types.Message):
    await message.answer(thursday_sub, parse_mode="Html")


@dp.message_handler(Text(equals=friday))
async def friday_schedule(message: types.Message):
    await message.answer(friday_sub, parse_mode="Html")


@dp.message_handler(Text(equals=saturday))
async def saturday_schedule(message: types.Message):
    await message.answer(saturday_sub, parse_mode="Html")


@dp.message_handler(Text(equals="Розклад на весь тиждень"))
async def full_week_schedule(message: types.Message):
    await message.answer(full_lessons_schedule, parse_mode="Html")


@dp.message_handler(Text(equals="Книги"))
async def books_command(message: types.Message):
    await message.answer(books, reply_markup=kb_books)
    await message.answer(attention)


@dp.message_handler(Text(equals=alg))
async def send_alg_book_command(message: types.document):
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


@dp.message_handler(Text(equals=geography))
async def send_geography_book_command(message: types.Message):
    await bot.send_document(message.chat.id, geography_book)


@dp.message_handler(Text(equals=world_hist))
async def send_world_hist_book_command(message: types.Message):
    await bot.send_document(message.chat.id, world_hist_book)


@dp.message_handler(Text(equals=ukr_hist))
async def send_ukr_hist_book_command(message: types.Message):
    await bot.send_document(message.chat.id, ukr_hist_book)


@dp.message_handler(Text(equals=it))
async def send_it_book_command(message: types.Message):
    await bot.send_document(message.chat.id, it_book)


@dp.message_handler(Text(equals=juris))
async def send_juris_book_command(message: types.Message):
    await bot.send_document(message.chat.id, jurisprudence_book)


@dp.message_handler(Text(equals=health))
async def send_health_book_command(message: types.Message):
    await bot.send_document(message.chat.id, health_book)


@dp.message_handler(Text(equals=exit))
async def exit_keyboard(message: types.Message):
    await message.answer("Головне меню", reply_markup=kb_start)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
