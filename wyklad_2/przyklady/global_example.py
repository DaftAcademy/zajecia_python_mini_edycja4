a = 5000

print(a)
print(80*'-')


def add_11_to_a():
    global a # bez tej linii będzie wyjątek
    a += 11
    print(a)
    print(80*'-')
    

add_11_to_a()

print(a)
print(80*'-')

    
