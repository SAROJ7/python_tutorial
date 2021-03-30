import json

people_string = '''
   {
       "people": [
            {
                "name": "Saroj Shrestha",
                "phone": "9843322391", 
                "emails": ["sarojsht377@gmail.com", "sarojsht277@gmail.com"], 
                "has_license": false
            },
            {
                "name": "Sanju Shrestha", 
                "phone": "9843036818", 
                "emails ": null, 
                "has_license": true
            }
        ]
    }
''' 
data = json.loads(people_string)
# print(type(data))
# print(data)
# print(data['people'])

for person in data['people']:
    print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)