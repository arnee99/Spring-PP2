import re

file = open('/Users/arnee/Desktop/Programming Principles II/week5/lab5/text.txt', 'r')

# 1. Write a Python program that matches a string 
# that has an 'a' followed by zero or more 'b''s.
# result = re.findall(".*a.*b*", file.read())
# print(result)

# 2. Write a Python program that matches a string 
# that has an 'a' followed by two to three 'b'.
# result = re.findall(".*a.*b.*b.*b?.*", file.read())
# print(result)

# 3. Write a Python program to find sequences of lowercase 
# letters joined with a underscore.
# result = re.findall("[a-z]+(_[a-z]+)+", file.read())
# print(result)

# 4. Write a Python program to find the sequences of one upper
# case letter followed by lower case letters.
# for i in file.read():
#     print(i)
# result = re.findall("[A-Z]+[a-z]+", file.read())
# print(result)

# 6. Write a Python program to replace all occurrences of 
# space, comma, or dot with a colon.
# result = re.sub("[ ,.]", ":", file.read())
# print(result)

# 7. Write a python program to convert snake case
# string to camel case string.
result = re.split("_", file.read())
print(result)

