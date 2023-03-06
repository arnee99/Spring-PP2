# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

yell = shout

print(yell('Hello!'))