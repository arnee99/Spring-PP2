# Python program to demonstrate
# Hierarchical inheritance
 
# Base class
class Parent:
    def function1(self):
        print("This function is in parent class.")
        
# Derived class #1
class Child1(Parent):
    def function2(self):
        print("This function is in child 1.")

#Derived class #2
class Child2(Parent):
    def function3(self):
        print("This function is in child 2.")
        
object1 = Child1()
object2 = Child2()
object1.function1()
object1.function2()

object2.function1()
object2.function3()