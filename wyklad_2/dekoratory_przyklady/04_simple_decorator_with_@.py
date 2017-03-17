print(80*'-')


def decorator(decorated_func):
    print('Wewnątrz dekoratora')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    def wrapper():
        print('Początek opakowania')
        tmp = decorated_func()
        print('Koniec opakowania')
        return tmp
        
    return wrapper # zwracamy funckcję wewnętrzną


print(80*'-')

@decorator
def hello_function():
    print('hello')
    
    
print(80*'-')
    
    
hello_function()
print(hello_function)
print(id(hello_function))
print(80*'-')

# "dekorator" bez @
# dekorator wykana jakiś kod (wpisanie dwóch stringów) w momencie dekorowania funkcji
# zwróci nowy obiekt funkcji pod "nazwę" dekorowanej funkcji
# od tego momentu udekorowana funkcja robi "coś więcej" niż pierwotnie
# pokazuje kiedy, który kod się wykona - teraz od razu po "zdefiniowaniu" funkcji
# przy każdym wywołaniu funkcji hello_function wykonuje się dodatkowy kod 
# "wstrzyknięty" przez dekorator


