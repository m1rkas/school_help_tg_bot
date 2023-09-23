from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from constants import *

b_exit = KeyboardButton(text=exit)

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
b1_start = KeyboardButton(text="Книги")
b2_start = KeyboardButton(text="Розклад")
kb_start.add(b1_start, b2_start)

kb_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
b1_schedule = KeyboardButton(text="Розклад уроків")
b2_schedule = KeyboardButton(text="Розклад дзвінків")
kb_schedule.add(b1_schedule, b2_schedule).add(b_exit)

kb_timetable = ReplyKeyboardMarkup(resize_keyboard=True)
b1_timetable = KeyboardButton(text="1 урок")
b2_timetable = KeyboardButton(text="2 урок")
b3_timetable = KeyboardButton(text="3 урок")
b4_timetable = KeyboardButton(text="4 урок")
b5_timetable = KeyboardButton(text="5 урок")
b6_timetable = KeyboardButton(text="6 урок")
b7_timetable = KeyboardButton(text="7 урок")
b8_timetable = KeyboardButton(text="Всі уроки")
kb_timetable.add(b1_timetable, b2_timetable, b3_timetable).add(b4_timetable, b5_timetable, b6_timetable).add(b7_timetable, b8_timetable).add(b_exit)


kb_group_choice = ReplyKeyboardMarkup(resize_keyboard=True)
b1_group = KeyboardButton(text="1 група")
b2_group = KeyboardButton(text="2 група")
kb_group_choice.add(b1_group, b2_group).add(b_exit)


kb_lessons_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
b1_lessons_schedule = KeyboardButton(text=monday)
b2_lessons_schedule = KeyboardButton(text=tuesday)
b3_lessons_schedule = KeyboardButton(text=wednesday)
b4_lessons_schedule = KeyboardButton(text=thursday)
b5_lessons_schedule = KeyboardButton(text=friday)
b6_lessons_schedule = KeyboardButton(text=saturday)
b7_lessons_schedule = KeyboardButton(text="Розклад на весь тиждень")
kb_lessons_schedule.add(b1_lessons_schedule, b2_lessons_schedule, b3_lessons_schedule).add(b4_lessons_schedule, b5_lessons_schedule, b6_lessons_schedule).add(b7_lessons_schedule).add(b_exit)

kb_books = ReplyKeyboardMarkup(resize_keyboard=True)
b1_books = KeyboardButton(text=alg)
b2_books = KeyboardButton(text=geom)
b3_books = KeyboardButton(text=phys)
b4_books = KeyboardButton(text=ukr_lang)
b5_books = KeyboardButton(text=ukr_lit)
b6_books = KeyboardButton(text=world_lit)
b7_books = KeyboardButton(text=biol)
b8_books = KeyboardButton(text=chem)
b9_books = KeyboardButton(text=geography)
b10_books = KeyboardButton(text=world_hist)
b11_books = KeyboardButton(text=ukr_hist)
b12_books = KeyboardButton(text=it)
b13_books = KeyboardButton(text=juris)
b14_books = KeyboardButton(text=health)
kb_books.add(b1_books, b2_books, b3_books).add(b4_books, b5_books, b6_books).add(b7_books, b8_books, b9_books).add(b10_books, b11_books, b12_books).add(b13_books, b14_books).add(b_exit)