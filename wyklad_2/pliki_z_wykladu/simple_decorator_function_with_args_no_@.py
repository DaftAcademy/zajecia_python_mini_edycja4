def decorator(decorated_func):
    print('dekoruję funkcję: {}'.format(decorated_func.__name__))
    
    def wrapper(*args, **kwargs):
        print('wewnątrz funkcji wrapper przed wykonaniem {}'.format(decorated_func.__name__))
        tmp = decorated_func(*args, **kwargs)
        print('wewnątrz funkcji wrapper po wykonaniu {}'.format(decorated_func.__name__))
        return tmp

    return wrapper
    
@decorator
def hello_1_arg(name):
    print('hello {}'.format(name))

@decorator
def hello_2_arg(name, surname):
    print('hello {} {}'.format(name, surname))
    
hello_1_arg('Zenon')
print(type(hello_1_arg))
print(id(hello_1_arg))
print(80*'-')

#hello_1_arg = decorator(hello_1_arg)
#hello_2_arg = decorator(hello_2_arg)

print(80*'-')

hello_1_arg('Zenon')
hello_2_arg('Zenon', 'Laskowik')
hello_2_arg('Zenon', surname='Laskowik')
print(type(hello_1_arg))
print(id(hello_1_arg))
print(80*'-')
    

