def hello_function(name):
    print('hello {}'.format(name))
    hello_function.count += 1
    
hello_function.count = 0    
say_hi = hello_function
say_hi('Antek')
#hello_function.count = 0
print(say_hi.count)

def greating_factory(hello):
    def greating(name):
        greating.count += 1
        print('{} {} {}'.format(hello, name, greating.count))
    greating.count = 0
    return greating
    
say_hi = greating_factory('hi')
say_hi('Antek')
say_hi('Kuba')
