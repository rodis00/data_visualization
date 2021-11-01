def foo(text):
    l_liter = 0
    l_wyrazow = 1
    srednia = 0
    for i in text:
        if i == ' ':
            l_wyrazow += 1
            continue
        else:
            l_liter += 1

    srednia = round(l_liter / l_wyrazow)
    print('liczba liter: '+str(l_liter) + '\nliczba wyrazow: '+str(l_wyrazow) + '\nsrednia dlugosc: ' + str(srednia) + '\n')




def foo2(text):
    dlugosci = [len(x) for x in text.split()]
    srednia = round(sum(dlugosci) / len(dlugosci))

    text_split = text.split()
    print(f'text: {text}\ntext_split: {text_split}\ndlugosci: {dlugosci}\nsrednia: {srednia}\n')


zd1 = "Ala ma kota"
zd2 = "Wlazł kotek na płotek"
zd3 = "Lorem ipsum dolor sit amet"

print(foo(zd1))
print(foo(zd2))
print(foo(zd3))
print('\n')
print(foo2(zd1))
print(foo2(zd2))
print(foo2(zd3))
