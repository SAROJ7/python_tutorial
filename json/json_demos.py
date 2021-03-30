import json

with open('states.json') as file_name:
    data = json.loads(file_name.read())

for state in data['states']:
    del state['area_codes']
    
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)