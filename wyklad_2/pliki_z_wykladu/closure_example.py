def greater_factory(greeting='hello'):
    def greater(name):
        print('{} {}'.format(greeting, name)) # LEGB
    return greater
    
hello_greater = greater_factory()
hi_greater = greater_factory('hi')

hello_greater('Janek')
hi_greater('Marysia')
hi_greater('Magda')
hello_greater('Kuba')


