from array import *
import random

n = int(input("Введіть число N (N > 12): "))

K = array('i', [])
M = array('i', [])
T = array('i', [])

for i in range(6):
    K.append(random.randint(12, n))

for i in range(24):
    M.append(random.randint(12, n))

for x in M:
    if x in K:
        T.append(x)

print("Масив K:", K)
print("Масив M:", M)
print("Масив T:", T)