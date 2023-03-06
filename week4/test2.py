class Person:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        def printInfo(self):
            print(self.color, self.number)
        def setWord(self, word):
            self.word = word
        def getWord(self):
            print(self.word)
class Parent1(Person):
    def __init__(self, color, number, word):
        Person.__init__(self, color, number)
        self.word = word
    def printInfo(self):
        print(self.color, self.number, self.word)
class Parent2(Person):
    def __init__(self, color, number, word):
        Person.__init__(self, color, number)
        self.word = word
    def printInfo(self):
        print(self.color, self.number, self.word)
class BabyBoy(Parent1, Parent2):
    def __init__(self, color, number, word):
        Person.__init__(self, color, number)
        self.word = word
    def printInfo(self):
        print(self.color, self.number, self.word)
obj1 = Parent1("Green", "72", "Bolshaya")
obj1.printInfo()
obj2 = Parent2("Maz", "21", "Buga")
obj2.printInfo()
obj3 = BabyBoy(obj1.color+obj2.color, obj1.number+obj2.number ,
               obj1.word+obj2.word)
obj3.printInfo()