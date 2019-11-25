from time import sleep
from random import randrange
from itertools import islice, tee

# tee() will return n independent iterators from a single iterable
# islice() allow you to cut out a piece of an iterable
nwise = lambda g, n = 2:zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
print(list(nwise('abcdef')))
window_averages = lambda g, n = 2: (sum(xs)/len(xs) for xs in nwise(g, n))

def compute():
    sleep(.1)
    return randrange(10)

def f():
    while True:
        yield compute()
    
for x in window_averages(f(), 3):
    print(x)
