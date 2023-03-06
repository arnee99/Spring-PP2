iterable = (1,2,3,4)
iterator_obj = iter(iterable)

print("Iterable loop 1:")
# iterating on iterable
for i in iterable:
    print(i, end = ',')
    
print("\nIterable Loop 2:")
for i in iterable:
    print(i, end = ',')

print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for i in iterator_obj:
    print(i, end = ',')
    
print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
print(next(iterator_obj))