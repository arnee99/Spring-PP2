import json

with open('data.json', 'r') as file:
    data = json.load(file)
    
print(type(data))
print(data)    