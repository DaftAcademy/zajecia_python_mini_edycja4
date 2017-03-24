def adder_factory(counter_type):
    count = [0]
    def adder(number):
        #nonlocal count # bez tej linijki poleci wyjątek
        count[0] += number
        print('{} {}!'.format(counter_type, count))
    return adder
        
hello_adder = adder_factory('hello')
hi_adder = adder_factory('hi')

hello_adder(1)
hi_adder(111)
hello_adder(4)
hi_adder(111)
