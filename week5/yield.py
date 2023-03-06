# A Simple Python program to demonstrate working
# of yield
 
# A generator function that yields 1 for the first time,
# 2 second time and 3 third time

def simpleGenerator():
    return "abc"
    return "cde"
    return "efg"

for value in simpleGenerator():
    print(type(value))
    print(value)