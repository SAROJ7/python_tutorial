import logging

logging.basicConfig(filename= 'text.log',level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add Functions"""
    return x+y

def subtract(x, y):
    """Subtract Functions"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Functions"""
    return x / 0



num1 = 20
num2 = 10

add_result = add(num1, num2)
logging.debug (f'Add: {num1} + {num2} = {add_result}')

sub_result = subtract(num1, num2)
logging.debug (f'Subtract: {num1} - {num2} = {sub_result}')

mul_result = multiply(num1, num2)
logging.debug (f'Multiply: {num1} * {num2} = {mul_result}')

try:
    div_result = divide(num1, num2)
except Exception as e:
    logging.debug (f'Divide: {num1} / {num2} = {num2}', exc_info=True)