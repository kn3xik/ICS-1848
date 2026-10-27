from datetime import date
from car import CAR

cars = [
    CAR("AA1234BB", "Octavia", "Skoda", 2008, "Петренко"),
    CAR("KA5678CK", "Focus", "Ford", 2015, "Іванченко"),
    CAR("BC9012AX", "Camry", "Toyota", 2019, "Сидоренко"),
    CAR("AE3456TT", "Golf", "Volkswagen", 2005, "Коваль"),
    CAR("AI7890KK", "Logan", "Renault", 2012, "Мельник"),
    CAR("BH1111EE", "Astra", "Opel", 2022, "Шевченко"),
]

cars[0].ChangeOwner("Бондаренко")
cars[1].ChangeNumber("KA0001CK")

cars.sort(key=lambda c: c.GetYear())
print("Усі автомобілі за роком випуску:")
for c in cars:
    c.DisplayProp()

current = date.today().year
print("\nАвтомобілі, вік яких перевищує 10 років:")
for c in cars:
    if current - c.GetYear() > 10:
        c.DisplayProp()
