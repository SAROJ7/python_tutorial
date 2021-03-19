
'''
First Class Function:
A programming language is said to have first call function if it treats the function as first class citizens.

First-Class Citizen(Programming):
"A first class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the 
operations generally available to othe entities. These operations typically include being passed as an argument, returned from a 
function, and assigned to a variable."
'''

def square(x):
    return x*x

g = square
f = square(5)
print(square)
print(f)
print(g(5))


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

def cube(x):
    return x*x*x

squares = my_map(cube, [1, 2, 3, 4, 5])

print (squares)

def logger(msg):

    def log_message():
        print('Log:',msg)
    
    return log_message

log_hi = logger('Hi!')
log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Heading')
print_h1('Second Heading')

print_p = html_tag('p')
print_p('First Paragraph')
print_p('Second Paragraph')

