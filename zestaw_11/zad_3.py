class Test:

    word = ''

    def getString(self):
        self.word = input('Podaj slowo: ')

    def printString(self):
        print(self.word.upper())



t1 = Test()
t1.getString()
t1.printString()
