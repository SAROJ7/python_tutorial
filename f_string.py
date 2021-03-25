from datetime import datetime

first_name ='Saroj'
last_name = 'Shrestha'

sentence = f'My name is {first_name.upper()} {last_name.upper()}.'
print(sentence)

person = {'name': 'Saroj', 'age': 24}

sentence = f"My name is {person['name']} and I am {person['age']} years old."

calculation = f'4 times 11 is equal to { 4*11}'
print(calculation)

for n in range(1,11):
    sentence = f'The value is {n:04}'
    print(sentence)

pi = 3.14159265

sentence = f'Pi is equal to {22 / 7:.51f}'
print(sentence)

birthday = datetime(1996, 7, 21)
sentence = f'Jenn has a birthday on {birthday:%B %d,%Y}'
print(sentence)