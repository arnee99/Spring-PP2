# Python program to demonstrate
# multilevel inheritance
 
# Base class
class Grandfather:
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName
        
# Intermediate class
class Father(Grandfather):
    def __init__(self, fatherName, grandFatherName):
        self.fatherName = fatherName
        super().__init__(grandFatherName)
        
# Derived class
class Child(Grandfather):
    def __init__(self, childName, grandFatherName):
        self.childName = childName
        super().__init__(grandFatherName)
        
    def print_names(self):
        print("Grandfather name is:", self.grandFatherName)
        # print("Father name is:", self.fatherName)
        print("Child name is:", self.childName)
        
ch = Child("Child", "Grandfather")
print(ch.grandFatherName)
ch.print_names()