cities = tuple(input("Введіть назви міст через пробіл: ").split())

d = {}
for city in cities:            # кожен елемент кортежу стає ключем словника
    d[city] = input(f"Введіть значення для '{city}': ")

print("\nСловник:")
for key, value in d.items():
    print(f"{key}: {value}")
