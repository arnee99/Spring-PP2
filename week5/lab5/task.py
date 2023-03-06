import re

file = open('/Users/arnee/Desktop/Programming Principles II/week5/lab5/text.txt', 'r')

# print(file.read())

# 1. Write a Python program that matches a string 
# that has an 'a' followed by zero or more 'b''s.
# print(re.search(r"^.*a(b*)", file.read()))
# final_list = re.findall(r".*a+.*", file.read())
# for element in final_list:
#     print(element)

# 2. Write a Python program that matches a string 
# that has an 'a' followed by two to three 'b'
# final_list = re.findall(r".*a+(.*b+){2,3}.*", file.read())
# final_list = re.findall(r".*a+.*b+.*b+.*b*.*", file.read())
# for element in final_list:
#     print(element)

# Write a Python program to find sequences of lowercase 
# letters joined with a underscore.
final_list = re.findall(r"([a-z]+_)+[a-z]+", file.read())
# for element in final_list:
#     print(element)
print(final_list)