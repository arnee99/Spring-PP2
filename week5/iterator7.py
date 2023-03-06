# Python code demonstrating
# basic use of iter()
l = ['a','e','i','o','u']

iter_l = iter(l)

try:
    print( next(iter_l))
    print( next(iter_l))
    print( next(iter_l))
    print( next(iter_l))
    print( next(iter_l))
    print( next(iter_l)) #StopIteration error
except:
    pass