# A Python program to demonstrate use of
# generator object with next()
 
# A generator function
def simpleGenerator():
    yield 1
    yield 2
    yield 3
    
# x is a generator object
x = simpleGenerator()

# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))