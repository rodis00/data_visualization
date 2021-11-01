import math


class Kolo:
    promien = 0

    def __init__(self, r):
        self.promien = r

    def pole(self):
        return self.promien ** 2 * math.pi


k1 = Kolo(2)
k2 = Kolo(10)

print(k1.pole())
print(k2.pole())
