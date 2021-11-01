def foo(*kwargs):
    list = []
    for kwargs in list:
        if kwargs not in list:
            list.append(kwargs)
    return list


l1 = [1, 2, 3, 2]
print(foo(l1))
