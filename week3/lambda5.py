lst = ["1", "2", "9", "0", "-1", "-2"]

print("Sorted numerically:",
    sorted(lst, key = lambda x : int(x)))

print("Filtered positive even numbers:",
    list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), 1)))

print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), 1)))