# Sample class with init method
class Person:
    
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print('Hello! My name is', self.name)
        
p = Person('Leila')
p.say_hello()