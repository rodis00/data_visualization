def foo(lista):
    wyraz = ''
    dlugosc = len(lista[0])
    for el in lista:
        if dlugosc > len(el):
            dlugosc = len(el)
            wyraz = el
    return wyraz


print(foo(['Ala', 'ma', 'kota']))
