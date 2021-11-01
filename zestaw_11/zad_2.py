def mnozenie(*lista):
    wynik = 1
    for el in lista:
        wynik *= el
    return wynik


print(mnozenie(2, 2))
