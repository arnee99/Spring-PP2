string = "Some random string"
ch_string = iter(string)

print(type(ch_string))
next(ch_string)
next(ch_string)
print(next(ch_string))
print(next(ch_string))
print(next(ch_string))