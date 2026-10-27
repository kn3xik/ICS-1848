line = input("Введіть назви країн через пробіл: ")
countries = tuple(sorted(line.split(), key=len))
for country in countries:
    print(country)
