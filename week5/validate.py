import re

email = input("What's your email?").strip()

# if re.search(r"^\w+@(\w+\.)?\w+\.(edu|kz|gov|net|org|com)$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
    
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
    
# if re.search("..*@..*", email):
#     print("Valid")
# else:
#     print("Invalid")
    