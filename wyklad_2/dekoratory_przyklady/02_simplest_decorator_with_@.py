print(80*'-')


def decorator(decorated_func):
    print('Wewnątrz dekoratora')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    return decorated_func


print(80*'-')


@decorator
def hello_function():
    print('hello')
    
    
print(80*'-')
    
    
hello_function()
print(hello_function)
print(id(hello_function))
hello_function()

# "dekorator" z @
# dekorator wykana jakiś kod (wpisanie dwóch stringów) w momencie dekorowania funkcji
# zwróci ten sam obiekt funkcji pod tę samą "nazwę"
# pokazuje kiedy, który kod się wykona - teraz od razu po "zdefiniowaniu" funkcji
