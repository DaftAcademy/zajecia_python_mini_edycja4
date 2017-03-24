def decorator(decorated_func):
    print('dekoruję funkcję: {}'.format(decorated_func.__name__))
    
    def wrapper():
        print('wewnątrz funkcji wrapper przed wykonaniem {}'.format(decorated_func.__name__))
        tmp = decorated_func()
        print('wewnątrz funkcji wrapper po wykonaniu {}'.format(decorated_func.__name__))
        return tmp

    return wrapper
    

@decorator    
def hello():
    print('hello world')
    
hello()
print(type(hello))
print(id(hello))
print(80*'-')

#hello = decorator(hello)

print(80*'-')

hello()
print(type(hello))
print(id(hello))
print(80*'-')
    

