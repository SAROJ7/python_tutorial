import os

if os.access('test.txt', os.R_OK):
    with open('test.txt') as f:
        print(f.read())
else:
    print('File cannot be accessed')


try:
    f = open('test1.txt')
except IOError as e:
    # print('File cannot be accessed')
    print(e)
else:
    with f:
        print(f.read())