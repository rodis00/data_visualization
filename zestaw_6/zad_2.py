import math

a = int(input('podaj a: '))
b = int(input('podaj b: '))
c = int(input('podaj c: '))
d = int(input('podaj d: '))

op1 = (a * b * c) * (1//8)
op2 = math.log(a**3) + math.log10(d)
op3 = math.sin(a)**2 + (math.cos(a)**2 + (d // math.sqrt(d)))

print(op1)
print(op2)
print(op3)


