def greater_factory(greeting='hello'):
    def greater(name):
        greater.count += 1
        print('{} {} {}'.format(greeting, name, greater.count)) # LEGB
    greater.count = 0
    return greater
    
hello_greater = greater_factory()
hi_greater = greater_factory('hi')

hello_greater('Janek')
print(hello_greater.count)
hi_greater('Marysia')
hi_greater('Magda')
hello_greater('Kuba')


