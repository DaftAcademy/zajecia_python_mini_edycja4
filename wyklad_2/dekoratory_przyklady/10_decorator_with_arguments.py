print(80*'-')


def my_wraps(base_function):
    # base_function to argument dekoratora my_wraps
    def outer_wrapper(wraps_decorated_function):
        print('początek outer_wrapper')
        def inner_wrapper(*args, **kwargs):
            print('Wewnątrz inner_wrapper')
            return wraps_decorated_function(*args, **kwargs)
        inner_wrapper.__name__ = base_function.__name__
        inner_wrapper.__module__ = base_function.__module__
        inner_wrapper.__doc__ = base_function.__doc__
        print('koniec outer_wrapper')
        return inner_wrapper
    
    return outer_wrapper


print(80*'-')


def hello_decorator(decorated_func):
    print('Wewnątrz dekoratora hello_decorator')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    #@my_wraps(decorated_func)
    def wrapper(*args, **kwargs):
        print('Mowię Ci hello')
        return decorated_func(*args, **kwargs)
        
    # zamiast zapisu z @ można uzyć:
    wrapper = my_wraps(decorated_func)(wrapper)
        
    return wrapper # zwracamy funckcję wewnętrzną


print(80*'-')


def goodbye_decorator(decorated_func):
    print('Wewnątrz dekoratora goodbye_decorator')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    @my_wraps(decorated_func)
    def wrapper(*args, **kwargs):
        tmp = decorated_func(*args, **kwargs)
        print('a potem goodbye')
        return tmp
    
    return wrapper # zwracamy funckcję wewnętrzną


print(80*'-')

@hello_decorator
@goodbye_decorator
def next_collatz(val):
    if not val % 2:
        n_val = int(val/2)
    else:
        n_val = 3 * val + 1
    print('{} -> {}'.format(val, n_val))
    return n_val

# poprawny
#next_collatz = hello_decorator(goodbye_decorator(next_collatz))
# błędny
#next_collatz = goodbye_decorator(hello_decorator(next_collatz))

  
print(80*'-')
a = next_collatz(2)
print(a)
print(80*'-')
print(next_collatz.__name__)



