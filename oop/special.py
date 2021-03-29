
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

    def __repr__(self):
        return f"Employee('{self.first}'','{self.last}',{self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Saroj', 'Shrestha', 50000)
emp2 = Employee('Deven', 'Shrestha', 6000)

print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())
print(emp1.__len__())
print(emp1)


print(int.__add__(1,2))
print(str.__add__('a', 'b'))

print(emp1 + emp2)