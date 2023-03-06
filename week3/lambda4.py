def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y

lambda_cube = lambda num: num ** 3
print(cube(30))
print(lambda_cube(30))