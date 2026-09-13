import sys

number_str = sys.argv[1]

d1 = int(number_str[0])
d2 = int(number_str[1])
d3 = int(number_str[2])
d4 = int(number_str[3])

product = d1 * d2 * d3 * d4
geom_mean = product ** (1 / 4)

print("Середнє геометричне цифр:", geom_mean)