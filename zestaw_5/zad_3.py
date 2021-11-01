class Wektor:
    a = 0
    b = 0

    def dodawanie(w1, w2):
        w = Wektor()
        w.a = w1.a + w2.a
        w.b = w1.b + w2.b
        return w


w1 = Wektor()
w1.a = 1
w1.b = 3
w2 = Wektor()
w2.a = 2
w2.b = 4
w3 = Wektor.dodawanie(w1, w2)

