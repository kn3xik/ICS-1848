import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

A = []
x = a
while x <= b:
    y = (math.cos(x) + math.exp(x)) / math.log2(abs(x) + 0.19)
    A.append(y)
    x = x + h

print("Список A (у стовпчик):")
for elem in A:
    print(elem)

B = A[:3] + A[-3:]

print("\nСписок B (перші 3 + останні 3 елементи A):")
print(B)