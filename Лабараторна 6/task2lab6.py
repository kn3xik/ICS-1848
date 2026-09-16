import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a
print("Табулювання функції:")
while x <= b:
    y = (math.cos(x) + math.exp(x)) / math.log2(abs(x) + 0.19)
    print("x=%.3f  y=%.5f" % (x, y))
    x = x + h