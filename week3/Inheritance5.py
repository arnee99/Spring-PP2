class C():
    def __init__(self):
        self.c = 21
        self.__d = 42
        
class D(C):
    def __init__(self):
        self.e = 84
        self.__d = 63
        C.__init__(self)
        
obj = D()
# print(obj.__d)
obj2 = C()
print(obj2.d)