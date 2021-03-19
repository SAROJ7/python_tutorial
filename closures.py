import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f'Running {func.__name__} with arguments {args}')
        print(func(*args))
    return log_func

def add(*args):
    x = 0
    for i in args:
        x += i
    return x

def mul(*args):
    x = 1
    for i in args:
        x *= i
    return x


add_logger = logger(add)
mul_logger = logger(mul)

add_logger(1, 2, 3, 4, 5, 6, 7)
add_logger(9, 7, 5, 4, 2)
add_logger(1231321, 42341, 12432)

mul_logger(23412, 234, 4435, 425)
mul_logger(8,6)