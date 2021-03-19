from functools import wraps

def decorator_function(outer_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapped executed this before {outer_function.__name__}')
        return outer_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display Function ran')

@decorator_function
def display_info(name, age):
    print(f'Display_info ran with arguments ({name},{age})')


display()
display_info('Saroj',24)

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_class
def displays():
    print('display Function ran')

displays()


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO) 
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)    
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrappers(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} secs')
        return result
    
    return wrappers

@my_logger
@my_timer
def display_info1(name, age):
    print(f'Display_info ran with arguments ({name},{age})')

display_info1('Sanjusht', 27)
