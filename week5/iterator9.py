# Python code demonstrating
# basic use of iter()
 
l = ['Cat', 'Bat', 'Sat', 'Mat']

iter_l = l.__iter__()

try:
    print(iter_l.__next__())
    print(iter_l.__next__())
    print(iter_l.__next__())
    print(iter_l.__next__())
    print(iter_l.__next__())
    print(iter_l.__next__())
    print(iter_l.__next__())
except:
    print(" \nThrowing 'StopIterationError'",
                     "I cannot count more.")