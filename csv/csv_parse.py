import csv

html_output = ''
names = []
names1 = []

html_output1 = ''


with open('patrons.csv', 'r') as datafile:
    csv_data = csv.reader(datafile)
    '''
    We don't want headers and first line of bad data
    '''
    for _ in range(2):
        next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break            
        names.append(f'{line[0]} {line[1]}')
html_output += f'<p> There are currently {len(names)} contributors. Thank You!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)


with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names1.append(f'{line["FirstName"]} {line["LastName"]}')
html_output1 += f'<p> There are currently {len(names1)} contributors. Thank You!</p>'
html_output1 += '\n<ul>'
for name in names1:
    html_output1 += f'\n\t<li>{name}</li>'

html_output1 += '\n</ul>'

print(html_output1)

