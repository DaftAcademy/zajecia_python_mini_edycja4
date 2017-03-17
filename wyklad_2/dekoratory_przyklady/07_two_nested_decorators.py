print(80*'-')


def hello_decorator(decorated_func):
    print('Wewnątrz dekoratora hello_decorator')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    def wrapper(*args, **kwargs):
        print('Mowię Ci hello')
        return decorated_func(*args, **kwargs)
        
    return wrapper # zwracamy funckcję wewnętrzną


print(80*'-')


def goodbye_decorator(decorated_func):
    print('Wewnątrz dekoratora goodbye_decorator')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
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

# dwa dekoratory jeden nad drugim


