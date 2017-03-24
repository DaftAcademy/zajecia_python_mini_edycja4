from functools import wraps

print(80*'-')


class hello_decorator():
    def __init__(self, decorated_func):
        self.decorated_func = decorated_func
        print('Creating hello_decorator')
    
    def __call__(self, *args, **kwargs):
        print('Mowię Ci hello')
        return self.decorated_func(*args, **kwargs)


print(80*'-')


def goodbye_decorator(decorated_func):
    print('Wewnątrz dekoratora goodbye_decorator')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    @wraps(decorated_func)
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

  
print(80*'-')
a = next_collatz(2)
print(a)
print(80*'-')



