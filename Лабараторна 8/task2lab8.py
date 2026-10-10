import numpy as np
import random

a = int(input("Введіть число a: "))

K = np.zeros((4, 6), dtype=int)
for i in range(4):
    for j in range(6):
        K[i][j] = random.randint(-a, a)

print("Масив K:")
print(K)

# збираємо індекси додатних елементів
indexes = []
for i in range(4):
    for j in range(6):
        if K[i][j] > 0:
            indexes.append([i, j])

B = np.array(indexes)

print("Масив B:")
print(B)