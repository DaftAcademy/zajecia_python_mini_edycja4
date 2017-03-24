from functools import wraps

print(80*'-')


class CallCounter():
    calls = {}
    def __init__(self, decorated_func):
        self.decorated_func = decorated_func
    
    def __call__(self, *args, **kwargs):
        # TODO: w tym miejscu może się wszystko sypnąć (polegamy na __name__, a nie
        # dbamy o to, żeby zostało zachowane
        self.calls[self.decorated_func.__name__] = 1 + self.calls.get(self.decorated_func.__name__, 0)
        return self.decorated_func(*args, **kwargs)


print(80*'-')


@CallCounter
def next_collatz(val):
    if not val % 2:
        n_val = int(val/2)
    else:
        n_val = 3 * val + 1
    print('{} -> {}'.format(val, n_val))
    return n_val

  
print(80*'-')
a = 19
count = 0
while a != 1:
    a = next_collatz(a)
    count += 1
    
print(80*'-')
print(CallCounter.calls)
print(count)



