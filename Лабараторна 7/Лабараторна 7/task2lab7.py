import random
import math
import string

s = input("Введіть повідомлення: ")

n = math.ceil(math.sqrt(len(s)))
total = n * n

while len(s) < total:
    s = s + random.choice(string.ascii_letters)

# розбиваємо на частини по N символів
parts = []
for i in range(0, total, n):
    parts.append(s[i:i + n])

print("Рядок після доповнення:", s)
print("Частини по", n, "символів:")
for p in parts:
    print(p)

print("Зашифроване повідомлення (по стовпчиках):")
for j in range(n):
    column = ""
    for p in parts:
        column = column + p[j]
    print(column)