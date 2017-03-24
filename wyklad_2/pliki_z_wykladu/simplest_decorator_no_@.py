def decorator(decorated_func):
    print('dekoruję funkcję: {}'.format(decorated_func.__name__))
    return decorated_func
    

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
    

