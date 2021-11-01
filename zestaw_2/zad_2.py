def foo(number):
    suma = 0
    while number > 0:
        a = number % 10
        number //= 10
        suma += a
    return suma


number = 34512
print(foo(number))
