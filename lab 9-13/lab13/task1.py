class PUPIL:
    def __init__(self, прізвище, ім_я, рік, клас):
        self.прізвище, self.ім_я, self.рік, self.клас = прізвище, ім_я, рік, клас

    def change_grade(self, новий_клас):
        self.клас = новий_клас

    def __str__(self):
        return f"{self.прізвище} {self.ім_я}, {self.рік} р.н., {self.клас} клас"


pupils = []
while True:
    c = input("1-Додати 2-Видалити 3-Змінити клас 4-Показати 0-Вихід: ")
    if c == "1":
        pupils.append(PUPIL(input("Прізвище: "), input("Ім'я: "),
                            int(input("Рік народження: ")), input("Клас: ")))
    elif c == "2":
        s = input("Прізвище: ").lower()
        pupils = [p for p in pupils if p.прізвище.lower() != s]
    elif c == "3":
        s = input("Прізвище: ").lower()
        for p in pupils:
            if p.прізвище.lower() == s:
                p.change_grade(input("Новий клас: "))
    elif c == "4":
        for p in pupils:
            print(p)
    elif c == "0":
        break