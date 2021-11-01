import math

a = float(input('podaj a: '))
b = float(input('podaj b: '))
c = float(input('podaj c: '))

op1 = (a ** 2 + math.sin(b)) / math.e ** c
op2 = math.atan(b ** (c ** 2))
op3 = math.log(c, a)

print(op1)
print(op2)
print(op3)
