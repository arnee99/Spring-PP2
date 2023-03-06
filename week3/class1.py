# Python3 program to
# demonstrate instantiating
# a class

class Dog:
    
    attr1 = "mammal"
    attr2 = "dog"
    
    def fun(self):
        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2)
        
    def bark(self):
        print("Woof, woof!")
        
Rodger = Dog()

print(Rodger.attr1, Rodger.attr2)
Rodger.fun()
Rodger.bark()