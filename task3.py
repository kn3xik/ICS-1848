import math
x = float(input("Ведіть значення x: "))

ctg_x = 1 / math.tan(x)
chyslennyk = 2.9 * x - ctg_x
znamenyk = 3 ** (0.7 * x + math.sqrt(x))

f = math.exp(x+ math.sqrt(x) + math.cos(x)) * (chyslennyk / znamenyk)

print("f(x) =", f)