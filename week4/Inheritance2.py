# Python program to demonstrate
# multiple inheritance
 
# Base class1
class Mother(object):
    mothername = ""
    
    def mother(self):
        print(self.mothername)
        
#Base class2
class Father(object):
    fathername = ""
    
    def father(self):
        print(self.fathername)
        
#Derived class
class Child(Mother):
    def parents(self):
        print("Father is:", self.fathername)
        print("Mother is:", self.mothername)
        
ch = Child()
ch.fathername = "Miguel"
ch.mothername = "Angelique"
ch.parents()