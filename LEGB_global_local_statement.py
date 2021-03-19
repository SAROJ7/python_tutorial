
'''
LEGB
Local, Enclosing, Global, Build-in
'''
import builtins

# print(dir(builtins))

x = 'global_x'
z = 'global z'

m = min([5,2,5,1,7,8])
print(m)

def test(a):
    global z
    y = 'local y'
    x = 'local x'
    z = 'local z'
    print(y)
    print(x)
    print(a)

test('local a')
print(x)
print(z)


def outer():
    x = 'outer x'
    z = 'outer z'
    def inner():
        nonlocal z 
        z = 'inner z'
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
    print(z)

outer()