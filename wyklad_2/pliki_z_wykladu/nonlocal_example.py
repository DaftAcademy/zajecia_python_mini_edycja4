def greater_factory(greeting='hello'):
    count = [0]
    def greater(name):
        count[0] += 1
        print('{} {} {}'.format(greeting, name, count)) # LEGB
    return greater
    
hello_greater = greater_factory()
hi_greater = greater_factory('hi')

hello_greater('Janek')
hi_greater('Marysia')
hi_greater('Magda')
hello_greater('Kuba')


