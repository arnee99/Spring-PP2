class Addition:
    first = 0
    second = 0
    answer = 0
    
    def __init__(self, f, s):
        self.first = f
        self.second = s
        
    def display(self):
        print("First number is: " + str(self.first))
        print("Second number is: " + str(self.second))
        print("Addition of two numbers: " + str(self.answer))
        
    def calculate(self):
        self.answer = self.first + self.second
        
# creating first object of same class       
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()