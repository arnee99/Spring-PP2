import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

person_dict = json.loads(person_string)
print(json.dumps(person_dict, indent=10, sort_keys=True))