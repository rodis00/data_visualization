def foo(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


print(foo(111))
