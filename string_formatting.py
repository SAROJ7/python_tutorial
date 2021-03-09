
### string formatting ###

greetings = 'Hello'
name = 'Saroj'

person = {'name': 'Saroj', 'age': 25 }
lit = ['Sanju', '25']

#string formatting of the dictionary. 

sentence  = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
newf  = f'My name is {name} and {greetings}'
newSentence = 'My name is {name} and I am {age} years old.'.format(**person)
#string formatting of the list.
new_sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(lit)
new_sentence1 = f'My name is {lit[0]} and I am {lit[1]} years old.'


message = '{} {}. Welcome!'.format(greetings, name)
print(sentence)
print(newf)
print(new_sentence)
print(new_sentence1)
print(newSentence)
print(message)
print(dir(name))



# string formating for the object
class person3():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person3('Jack', '33')

sentence1 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)

print(sentence1)


#string formatting for the keyword
sentence2 = 'My name is {name} and I am {age} years old.'.format(name="Jack",age=23)
print(sentence2)

#digit formatting
for i in range(1, 11):
    sentence3 = 'The value is {:02}'.format(i)
    print(sentence3)

pi = 3.14159265

#Decimal Place Formatting
sentence4 = 'The value of pi is {:.2f}'.format(pi)
print(sentence4)

#Comma Formatting
sentence5 = 'The ICX can be divided into {:,.2f} pieces'.format(10 ** 18)
print(sentence5)


#Date/Time Formatting
import datetime

mydate = datetime.datetime(2016, 4, 14, 12, 30, 46) 
sentence6 = '{:%B %d,%Y}'.format(mydate)
sentence7 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
print(sentence6)
print(sentence7)

print(dir(datetime))