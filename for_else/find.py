
def find_index(to_search, target):
    for i,value in enumerate(to_search, start=1):
        if value == target:
            break
    else:
        return -1
    return i


my_list = ['Saroj', 'Sanju', 'Sagar']
index_location = find_index(my_list, 'Sagar')

print(f'Location of target is index:{index_location}')