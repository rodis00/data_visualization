
def funkcja(lista1, lista2):
    return list(zip(lista1, lista2))


def funkcja2(lista1, lista2):
    temp = []
    for j in range(0, len(lista1)):
        temp.append((lista1[j], lista2[j]))

    return temp


x = ['A', 'B', 'C']
y = ['x', 'y', 'z']
print(funkcja(x, y))
print(funkcja2(x, y))
