from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from constants import *

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
b1_start = KeyboardButton(text="Книги")
kb_start.add(b1_start)

kb_books = ReplyKeyboardMarkup(resize_keyboard=True)
b1_books = KeyboardButton(text=alg)
b2_books = KeyboardButton(text=geom)
b3_books = KeyboardButton(text=phys)
b4_books = KeyboardButton(text=ukr_lang)
b5_books = KeyboardButton(text=ukr_lit)
b6_books = KeyboardButton(text=world_lit)
b7_books = KeyboardButton(text=biol)
b8_books = KeyboardButton(text=chem)
b9_books = KeyboardButton(text=geo)
b10_books = KeyboardButton(text=world_hist)
b11_books = KeyboardButton(text=ukr_hist)
b12_books = KeyboardButton(text=it)
b13_books = KeyboardButton(text=exit)
kb_books.add(b1_books, b2_books, b3_books).add(b4_books, b5_books, b6_books).add(b7_books, b8_books, b9_books).add(b10_books, b11_books, b12_books).add(b13_books)