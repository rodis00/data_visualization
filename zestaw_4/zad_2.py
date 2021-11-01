def foo(*lista):
    min1 = min(lista)
    max1 = max(lista)
    r = abs(min1-max1)
    return r



print(foo(2, 3, 4, 4, -2, 8, 10))
print(foo(2, 3))
print(foo(5))
print(foo(1, 2, -3, 40))


