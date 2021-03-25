
try:
    f = open('test_file.txt', 'r')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally.....')



try:
    f = open('currupt_file.txt', 'r')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception :
    print('Something went wrong!')
else:
    print(f.read())
    f.close()
finally:
    print(f'{f.name}')