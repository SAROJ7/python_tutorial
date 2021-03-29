

class Employee:

    raise_amount = 1.04
   

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())
    





dev1 = Developer('Saroj', 'Shrestha', 50000, 'Python')
dev2 = Developer('Deven', 'Shrestha', 6000, 'C')

mgr1 = Manager('Sanju', 'Shrestha', 90000, [dev1])

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)

print(mgr1.email)
mgr1.print_emps()

# print(help(Developer))
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(dev2.prog_lang)
print(dev2.email)

print(isinstance(mgr1, Employee))
print(issubclass(Manager, Employee))