import re

#url = "https://twitter.com/kanyewest"
url = input("Please, insert url: ")

if re.search(r"^(https|http)://(www)?.+\.(com|kz|ru|org|net)/[a-zA-Z0-9]+$", url, re.IGNORECASE):
    print("Valid!")
else:
    print("Invalid!")