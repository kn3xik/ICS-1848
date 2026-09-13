import math

def compute_L(x,y,z,a) :
    chyselnyk = math.tan(y) + math.e ** a
    znamenyk = 2 ** (z + 2.4)
    L = (x * math.cos(y) + z) - (chyselnyk / znamenyk)
    return L

x = float(input("ведіть значення x: "))
y = float(input("ведіть значення y: "))
z = float(input("ведіть значення z: "))
a = float(input("ведіть значення a: "))

L = compute_L(x,y,z,a)
print("L =", L)