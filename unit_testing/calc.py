
def add(x, y):
    """Add Functions"""
    return x+y

def subtract(x, y):
    """Subtraction Function"""
    if x < y:
        raise ValueError(f'{x} is smaller than {y}')
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if  y == 0 :
        raise ValueError('Cannot Divide by 0')
    return x / y

