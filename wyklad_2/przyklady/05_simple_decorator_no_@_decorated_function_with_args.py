print(80*'-')


def decorator(decorated_func):
    print('Wewnątrz dekoratora')
    print('dekorowana funkcja {}'.format(decorated_func.__name__))
    
    def wrapper(*args, **kwargs):
        print('Początek opakowania funkcji: {}, argumenty: {}'.format(
                decorated_func.__name__, args)
        )
        tmp = decorated_func(*args, **kwargs)
        print('Koniec opakowania')
        return tmp
        
    return wrapper # zwracamy funckcję wewnętrzną


print(80*'-')


def hello_function_1_arg(name):
    print('hello {}'.format(name))
    

def hello_function_2_arg(name, surname):
    print('hello {} {}'.format(name, surname))

    
print(80*'-')
    
    
hello_function_1_arg('Jan')
print(hello_function_1_arg)
print(id(hello_function_1_arg))
print(80*'-')
hello_function_2_arg('Jan', 'Kowalski')
print(hello_function_2_arg)
print(id(hello_function_2_arg))
print(80*'-')

decorator(hello_function_1_arg)('Zenon')
decorator(hello_function_2_arg)('Zenon', 'Laskowik')
decorator(hello_function_2_arg)(name='Zenon', surname='Laskowik')
print(80*'-')
hello_function_1_arg('Jan')
print(hello_function_1_arg)
print(id(hello_function_1_arg))
print(80*'-')
hello_function_2_arg('Jan', 'Kowalski')
print(hello_function_2_arg)
print(id(hello_function_2_arg))
print(80*'-')
print(80*'-')
hello_function_1_arg = decorator(hello_function_1_arg)
hello_function_2_arg = decorator(hello_function_2_arg)

print(80*'-')
hello_function_1_arg('Jan')
print(hello_function_1_arg)
print(id(hello_function_1_arg))
print(80*'-')
hello_function_2_arg('Jan', 'Kowalski')
print(hello_function_2_arg)
print(id(hello_function_2_arg))
print(80*'-')

hello_function_2_arg(surname='Kowalski', name='Jan')
print(hello_function_2_arg)
print(id(hello_function_2_arg))
print(80*'-')

# "dekorator" bez @
# dekorator wykona jakiś kod (wpisanie dwóch stringów) w momencie dekorowania funkcji
# zwróci nowy obiekt funkcji pod "nazwę" dekorowanej funkcji
# od tego momentu udekorowana funkcja robi "coś więcej" niż pierwotnie
# pokazuje kiedy, który kod się wykona - teraz od razu po "zdefiniowaniu" funkcji
# przy każdym wywołaniu funkcji hello_function wykonuje się dodatkowy kod 
# "wstrzyknięty" przez dekorator
# dekorator może teraz dekorowac funkcje od dowolnej liczbie argumentów pozycyjnych
# dla argumentów keyword trzeba dodać **kwargs do wrappera i wywołania dekorowanej
# funkcji w wrapperze


