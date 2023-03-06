# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

#class for Dog

class Dog:
    
    animal = 'Dog'
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)