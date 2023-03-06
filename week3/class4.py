# Python3 program to show that we can create
# instance variables inside methods
 
# Class for Dog

class Dog:
    
    animal = 'Dog'
    
    def __init__(self, breed):
        self.breed = breed
        
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
print(Rodger.color)