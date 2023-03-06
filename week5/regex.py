import re
email = input("Please, write your email: ")

# if "@" in email and ".kz" in email:
#     print("Valid!")
# else:
#     print("Invalid!")

if re.search(r"^[a-zA-Z_0-9]+@[a-z]+\.(com|ru|kz|org|net)$", email):
    print("Valid!")
else:
    print("Invalid!")
'''
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.
[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:
[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-
\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-
\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*
[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*
[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4]
[0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.)
{3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]
|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:
(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a
\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
'''
