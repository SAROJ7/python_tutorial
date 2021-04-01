import logging
import employee

#Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create Handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('sample.log', mode='w')
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)

#Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

#Add Handler to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to Divide by 0')
    else:
        return result



num1 = 20
num2 = 0

add_result = add(num1, num2)
logger.debug (f'Add: {num1} + {num2} = {add_result}')

sub_result = subtract(num1, num2)
logger.debug (f'Subtract: {num1} - {num2} = {sub_result}')

mul_result = multiply(num1, num2)
logger.debug (f'Multiply: {num1} * {num2} = {mul_result}')

div_result = divide(num1, num2)
logger.debug (f'Divide: {num1} / {num2} = {div_result}')
