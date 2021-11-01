class Calculator:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def calculate_power(self):
        return self.var1 ** self.var2

    def calculate_sum(self, var3):
        return self.var1 + self.var2 + var3


calc = Calculator(2, 3)
print(calc.calculate_power() == 8)
print(calc.calculate_sum(4) == 9)

