def myFun(**kwargs):
    """A function that was built to return some values"""
    for key, value in kwargs.items():
        print(key, value)
        
myFun(first = 'WallE', mid = 'The', last = 'Robot')

print(myFun.__doc__)