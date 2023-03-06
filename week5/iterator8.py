# Python code demonstrating
# basic use of iter()
l = [11, 22, 33, 44, 55]

iter_l = iter(l)
while True:
    try:
        print(iter_l.__next__())
    except:
        break