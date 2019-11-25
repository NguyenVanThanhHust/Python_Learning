__my_name__ = 'Nguyen Van Thanh'
__mail__ = "NguyenVanThanhHust@gmail.com"
__content__ = "done use this code"

def add1(x, y):
    return x + y

add2 = lambda x, y: x + y

from time import sleep
from random import randrange
def compute():
    sleep(.1)
    return randrange(10)

# normal result: this way is slower becasue in line 19, 
# we compute and store all value, test by put a break in for loop
def f():
    rv = []
    for _ in range(10):
        rv.append(compute())
    return rv

for x in f():
    print(x)

print('-' * 80)
# use iterator to calculate: this way is faster because it only calculate 
# when we need it
class F:
    def __iter__(self):
        self.size = 10
        return self
    def __next__(self):
        if not self.size:
            raise StopIteration
        self.size -= 1
        return compute()

f = F()
for x in f:
    print(x)
#     print(x)
# print(f'add 1: {add1(1, 2)}')
# print(f'add 2: {add2(1, 2)}')
# print(f'f: {f()}')