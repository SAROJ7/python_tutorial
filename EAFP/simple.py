
# person = {'name': 'Saroj', 'age':24, 'job':'Programmer'}
person = {'name': 'Sanju', 'age':24}

if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
else:
    print('Missing some keys')

try:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
except KeyError as e:
    print(f'Missing {e} key')


my_list = [1, 2, 3, 4, 5, 6]

if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

try:
    print(my_list[3])
except IndexError:
    print('That index doesnot exists')
