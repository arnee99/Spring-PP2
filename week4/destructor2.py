class Animal:
    
    def __init__(self):
        self.cat = Cat
        print('The class called Animals is called.')
        
    def __del__(self):
        print('The destructor is called for deleting Animals')

class Cat(Animal):
    def __init__(self, animal):
        self.animal = animal
        super().__init__()
        print("Cat was created!")
    
    def __del__(self):
        print("The cat id dead! :(")
        
# def createObject():
#     print('we are creating an object.')
#     object = Animal()
#     print('we are ending a function here.')
#     return object

# object = createObject()
# print('The program is ending here')
animal = Animal()
cat = Cat(animal)
