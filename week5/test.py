a = [10, 20, 30, 40]

# for i in enumerate(a):
obj1 = range(len(a))
obj2 = enumerate(a)

for i in obj1:
    if i == 1:
        break
    
for i in obj2:
    if i[0] == 1:
        break
    
for i in obj1:
    print(i)
    
print("\n")
    
for i in obj2:
    print(i)

# a = [10, 20, 30, 40]

# count = 0
# for val in a:
#     print(count, val)
#     count += 1