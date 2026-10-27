from math import sqrt


def area(a):
    return 3 * sqrt(3) / 2 * a ** 2


def diagonals(a):
    return [a * sqrt(3)] * 6 + [2 * a] * 3


a = float(input("Сторона шестикутника: "))
print(f"Площа: {area(a):.3f}")
for i, d in enumerate(diagonals(a), 1):
    print(f"Діагональ {i}: {d:.3f}")
