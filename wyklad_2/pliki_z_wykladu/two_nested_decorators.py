def hello_decorator(decorated_func):
    print('hello_decorator dekoruję funkcję: {}'.format(decorated_func.__name__))
    
    def wrapper(*args, **kwargs):
        print('Mówię Ci hello'.format(decorated_func.__name__))
        tmp = decorated_func(*args, **kwargs)
        return tmp

    return wrapper
    
def goodbye_decorator(decorated_func):
    print('goodbye_decorator dekoruję funkcję: {}'.format(decorated_func.__name__))
    
    def wrapper(*args, **kwargs):
        tmp = decorated_func(*args, **kwargs)
        print('A potem goodbye'.format(decorated_func.__name__))
        return tmp

    return wrapper

@goodbye_decorator
@hello_decorator
def hello_2_arg(name, surname):
    print('hello {} {}'.format(name, surname))
    
#hello_2_arg = hello_decorator(goodbye_decorator(hello_2_arg))
hello_2_arg('Zenon', 'Laskowik')
    

