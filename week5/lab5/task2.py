import re

file = open('/Users/arnee/Desktop/Programming Principles II/week5/lab5/text.txt', 'r')

# 1. Write a Python program that matches a string that
# has an 'a' followed by zero or more 'b''s.
# result = re.findall(".*a.*b.*", file.read())
# print(result)


# 2. Write a Python program that matches a string 
# that has an 'a' followed by two to three 'b'.
# result = re.findall(".*a.*b+.*b+.*b*.*", file.read())
# result = re.findall(".*a.*b+.*b+.*", file.read())
# result = re.findall(".*a.*b.*b.*|.*a.*b.*b.*b.*", file.read())
# print(result)

# 3. Write a Python program to find sequences of 
# lowercase letters joined with an underscore.
# result = re.findall("[a-z]+_[a-z]+", file.read())
# print(result)

# 4. Write a Python program to find the sequences 
# of one upper case letter followed by lower case letters.
# result = re.findall("[A-Z]{1}[a-z]+", file.read())
# print(result)

# 5. Write a Python program that matches a string
# that has an 'a' followed by anything, ending in 'b'.
result = re.findall(r".*a.*b$", file.read())
print(result)