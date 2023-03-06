# Python program to
# demonstrate private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksForGeeks"
        self.__a = "ShmeeksForShmeeks"
        print(self.__a)
    
    def changePrivate(self):
        self.__a = "New text"
        
# Creating a Derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)
        
# obj1 = Derived()
# print(obj1.__a)

obj = Base()