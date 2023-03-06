tup = ('a', 'b', 'c', 'd', 'e')

# iterating on each item of the iterable (here: tuple)
# for item in tup:
#     print(item)

iter_tup = iter(tup)   
next(iter_tup)
print(next(iter_tup))