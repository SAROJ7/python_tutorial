from operator import attrgetter


li = [ 9,4,3,6,2,26,1,12,7,7,43,2]
s_li= sorted(li)
print(f'Sorted list {s_li}')
print(f'Original list {li}')

tupl = (9,5,1,7,8,9,1,4,6,3,1,0)
s_tupl = sorted(tupl)
print(f'Original Tuple {tupl}')
print(f'Sorted Tuple {s_tupl}')

di = {'name': 'Saroj', 'job': 'Programming', 'age': None, 'os': 'Linux'}
s_di = sorted(di)
print(f'Sorted Dictionary: {s_di}')

li = [ -6, -5, -4, 1, 2, 3]
s_li = sorted(li, key= abs)
print(f'Sorted List: {s_li}')


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return (f'{self.name}, {self.age}, ${self.salary}')

e1 = Employee('Saroj', 24, 500)
e2 = Employee('Sanju', 23, 600)
e3 = Employee('Santosh', 30, 150)
employees = [e1, e2, e3]

def esalary_sort(emp):
    return emp.salary

s_employees = sorted(employees, key = attrgetter('name'))
s_employees1 = sorted(employees, key = lambda e: e.age)
s_employees2 = sorted(employees, key = esalary_sort, reverse= True)
print(f'Sorted with key = name as :{s_employees}')
print(f'Sorted with key = age as :{s_employees1}')
print(f'Sorted with key = salary as :{s_employees2}')


