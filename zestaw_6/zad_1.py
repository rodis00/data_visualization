
def foo(liczba):
    liczba = int(liczba)
    print(liczba, 'jest typu int: ', isinstance(liczba, int))


liczba = input('podaj liczbe: ')
foo(liczba)
