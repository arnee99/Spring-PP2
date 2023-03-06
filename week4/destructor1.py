# we will illustrate destructor function in Python program  
# we will create Class named Animals  

class Animals:
    # firstly, we will initialize a class
    def __init__(self):
        print("The class called Animal is created.")
        
    #now, we will call a destructor
    def __del__(self):
        print("The destructor is called for deleting the animal.")
    
object = Animals()
del object