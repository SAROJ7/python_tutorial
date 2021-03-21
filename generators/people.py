import mem_profile
import random
import time

names = ['Saroj','Deven','Sanam','Syasu','Rupesh','Rishav']
major = ['Programming', 'Networking', 'Cloud Computing', 'Internet Technology', 'Artificial Intelligence']

print(f'Memory (Before): {mem_profile.memory_usage_psutil()}Mb')

def people_list(num_people):
    result = []
    for _ in range(num_people):
        person = {
            'id' : 1,
            'name': random.choice(names),
            'major': random.choice(major)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for _ in range(num_people):
        person = {
            'id' : 1,
            'name' : random.choice(names),
            'major': random.choice(major)
        }
        yield person

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

print (f'Memory (After) : {mem_profile.memory_usage_psutil()}Mb')
print (f'Took {t2-t1} Seconds')

t3 = time.time()
people = people_generator(1000000)
t4 = time.time()

print (f'Memory (After) : {mem_profile.memory_usage_psutil()}Mb')
print (f'Took {t4-t3} Seconds')