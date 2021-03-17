
courses = ['History', 'Math', 'Physics', 'ComputerScience']
courses_2 = ['Moral', 'Nepali', 'Finance']
courses_3 = ['Social', 'Chemistry']
courses.append('art')
print(courses)
courses.insert(0, 'Database')
courses.insert(0, courses_2)
courses.extend(courses_3)
print(courses)
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[::-1])
courses.remove('Math')
print(courses)
courses.pop()
print(courses)
popped = courses.pop()
print(popped)
print(courses)
courses_2.sort()
print(courses_2)
courses.reverse()
print(courses)

nums = [5,52,62,2,1,7,9,21,442,52,34,12,452]
nums.sort(reverse = True)
print(nums)

sorted_courses = sorted(courses_3)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses_3.index('Social'))
print('Art' in courses_3)
print('Chemistry' in courses_3)

for item in courses_3:
    print(item)

for index, course in enumerate(courses_2):
    print(index, course)

for index, course in enumerate(courses_2, start = 1):
    print(index, course)

course_str = '_'.join(courses_2)
print(course_str)

new_list = course_str.split('_')
print(new_list)

#tuple is immutable 

#sets
cs_courses = {'History', 'Math' , 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#Empty Set
empty_set = {} #This isn't right. It refers to the dictionary 
empty_set = set()
