import json

with open('data.json', 'r') as file:
    data = json.load(file)

# person_dict = {
#     "name": "Bob",
#     "languages": ["English", "French"],
#     "married": True,
#     "age": 32
# }

print(data)
data['test'] = 'test'
 
with open('person.json', 'w') as json_file:
    json.dump(data, json_file)