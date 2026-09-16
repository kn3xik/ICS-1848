import math
a = float(input("Задайте a: "))
b = float(input("Задайте b: "))
h = float(input("Задайте h: "))

d = int((b-a) / h) + 1

print("Табулювання функції:")
for i in range(d):
    x = a + i * h
    y = (math.cos(x) + math.exp(x)) / math.log2(abs(x) + 0.19)
print("i=%d x=%.3f y=%.5f" % (i, x, y))