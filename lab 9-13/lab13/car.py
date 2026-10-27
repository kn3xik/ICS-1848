# Лабораторна робота №13, варіант 20, завдання 2 - модуль з класом CAR
class CAR:
    def __init__(self, number, model, producer, year, owner):
        self.Number = number
        self.Model = model
        self.Producer = producer
        self.Year = year
        self.Owner = owner

    def ChangeNumber(self, new_number):
        self.Number = new_number

    def ChangeOwner(self, new_owner):
        self.Owner = new_owner

    def DisplayProp(self):
        print(f"Номер: {self.Number}, модель: {self.Model}, "
              f"виробник: {self.Producer}, рік: {self.Year}, "
              f"власник: {self.Owner}")

    def GetYear(self):
        return self.Year

    def GetOwner(self):
        return self.Owner
