def foo(*kwargs):
    list = []
    for kwarg in kwargs:
        if kwarg not in list:
            list.append(kwarg)
    return list


l1 = [1, 2, 3, 2]
print(foo(l1))
