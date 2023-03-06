# filter_nums = lambda s: ''.join([ch for ch in s if ch.isdigit()])
# print("filter_nums():", filter_nums("I love Python3!"))

# do_exclaim = lambda s: s + '!'
# print("do_exclaim():", do_exclaim("I am soooo tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(123))