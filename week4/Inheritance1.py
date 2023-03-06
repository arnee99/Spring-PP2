# Python program to demonstrate
# single inheritance
 
# Base class
class Parent:
    def function1(self):
        print("This function is in parent class.")
        
# Derived class
class Child(Parent):
    def function2(self):
        print("This function is in child class.")
        
object = Child()
object.function1()
object.function2()