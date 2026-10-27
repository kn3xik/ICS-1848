import csv, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
F = "phone.csv"

def load():
    return list(csv.reader(open(F, encoding="utf-8"), delimiter=";")) if os.path.exists(F) else []

def save(r):
    csv.writer(open(F, "w", newline="", encoding="utf-8"), delimiter=";").writerows(r)

book = load()
while True:
    c = input("1-Показати 2-Додати 3-Пошук 4-Видалити 0-Вихід: ")
    if c == "1":
        for r in book: print(*r)
    elif c == "2":
        book.append([input("Прізвище: "), input("Ім'я: "), input("Телефон: ")])
        save(book)
    elif c == "3":
        s = input("Що шукати: ").lower()
        for r in book:
            if s in " ".join(r).lower(): print(*r)
    elif c == "4":
        s = input("Прізвище: ").lower()
        book = [r for r in book if r[0].lower() != s]
        save(book)
    elif c == "0":
        break