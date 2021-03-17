
#String is immutable
a = 'Saroj'
print (a)
print (f'Address of a is {id(a)}')
a = 'Sanju'
print(a)
print (f'Address of a is {id(a)}')

#list is mutable
b = [1, 2, 3, 4, 5]
print(b)
print(f'Address of b is {id(b)}')
b[0]= 6
print(b)
print(f'Address of b is {id(b)}')


employees = ['Saroj', 'Deven', 'Sanam', 'Syasu', 'Pramod', 'Eric']

output = '<ul>\n'

for employee in employees:
    output += f'\t<li>{employee}</li>\n'
    print (f'Addresses of output is {id(output)}')

output += '</ul>'

print(output)

print('\n')