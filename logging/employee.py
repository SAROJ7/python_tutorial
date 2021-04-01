import logging

#Create a custom logger
logger = logging.getLogger(__name__)


#create Handler
file_handler = logging.FileHandler('employee.log')
file_handler.setLevel(logging.INFO)

#Create formatters and add it to handlers
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

#Add Handler to the logger
logger.addHandler(file_handler)

class Employee:
    """A Sample Employee class"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info(f'Created Employee: {self.fullname} - {self.email}')
    

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'



emp1 = Employee('Saroj', 'Shrestha')
emp2 = Employee('Shrestha', 'Sanju')
emp3 = Employee('Syasu', 'Buddhathoki')