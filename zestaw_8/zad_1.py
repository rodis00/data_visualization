def gwiazdki(a):
    for i in range(a):
        for j in range(i+1):
            print('*', end='')
        print('')

    for i in range(a-1):
        for j in range(a-1):
            print('*', end='')
        print('')
        a -= 1


gwiazdki(5)
