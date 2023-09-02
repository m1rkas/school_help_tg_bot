greeting = """
Привіт. 
Натисни на кнопку 'Книги' і в тебе з'явиться список предметів, вибери один, та бот надішле pdf файли книги з цього предмету."""

books = """
Виберіть предмет, і бот надішле pdf file підручника з цього предмету."""

attention = """
УВАГА!
Файли з підручниками відправляються НЕ одразу, а протягом певного часу(в середньому 10-15 секунд, залежить від інтернету)."""

exit = "Назад"

# Назва предметів

alg = "Алгебра"
geom = "Геометрія"
phys = "Фізика"
ukr_lang = "Українська мова"
ukr_lit = "Українська література"
world_lit = "Зарубіжна література"
biol = "Біологія"
chem = "Хімія"
geo = "Географія"
world_hist = "Всесвітня історія"
ukr_hist = "Історія України"
it = "Інформатика"

# Підручники

alg_book = open("books/Algebra.pdf", "rb")
geom_book = open("books/Geometry.pdf", "rb")
phys_book = open("books/Physics.pdf", "rb")
ukr_lang_book = open("books/Ukr_lang.pdf", "rb")
ukr_lit_book = open("books/Ukr_lit.pdf", "rb")
world_lit_book = open("books/World_lit.pdf", "rb")
biol_book = open("books/Biology.pdf", "rb")
chem_book = open("books/Chemistry.pdf", "rb")
geo_book = open("books/Geography.pdf", "rb")
world_hist_book = open("books/World_history.pdf", "rb")
ukr_hist_book = open("books/Ukr_history.pdf", "rb")
it_book = open("books/It.pdf", "rb")