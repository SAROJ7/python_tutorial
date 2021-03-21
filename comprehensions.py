
#list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)

my_list1 = [n for n in nums]

print(my_list)
print(my_list1)

mylist2 = [n for n in nums if n%2 == 0]
print(mylist2)

mylist3 = [(letter,num) for letter in 'abcd' for num in range(4)]
print(mylist3)

#dictionary comprhension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(tuple(zip(names, heros)))

my_dict = {name: hero for name,hero in list(zip(names, heros)) if name != 'Logan'}
print(my_dict)

#set comprehension
numset = [1,2,1,3,4,4,4,5,1,1,1,3,3,7,7,7,8,8,9,99]

my_set= [n for n in numset]
print(my_set)


#generator expressions
numgenerator = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(numgenerator):
#     for n in numgenerator:
#         yield n*n
# my_gen = gen_func(numgenerator)    
my_gen = (n*n for n in numgenerator)

for i in my_gen:
    print (i)

