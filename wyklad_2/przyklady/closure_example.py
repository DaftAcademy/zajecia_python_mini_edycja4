def greater_factory(gerating='hello'):
    def greater(name):
        print('{} {}!'.format(gerating, name))
    return greater
        
hello_greater = greater_factory('hello')
hi_greater = greater_factory('hi')

hello_greater('Janek')
hi_greater('Magda')
hello_greater('Maciek')
