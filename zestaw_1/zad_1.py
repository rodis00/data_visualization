'ax^2 + bx + c'
from math import sqrt


def foo(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('delta ujemna brak rozwiązań')
    elif delta == 0:
        x1 = ((-1 * b) - sqrt(delta)) / (2 * a)
        print(f'x = {x1}')
    else:
        x1 = ((-1 * b) - sqrt(delta)) / (2 * a)
        x2 = ((-1 * b) + sqrt(delta)) / (2 * a)
        print(f'x1 = {x1}\nx2 = {x2}')


print('podaj wartości wielomianu ax^2 + bx + c')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

foo(a, b, c)
