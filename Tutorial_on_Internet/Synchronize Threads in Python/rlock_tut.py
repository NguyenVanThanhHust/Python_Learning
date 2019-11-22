# https://medium.com/better-programming/synchronization-primitives-in-python-564f89fee732

import threading

num = 0
lock = threading.Lock()

# This example to show that lock will block all thread even the same thread holding the lock
lock.acquire()
num += 1
print("num 1: ", num)
print("next computation won't be activated, print ctrl + C, comment this block and re run")
lock.acquire()
num += 2
print("num 2: ", num)
lock.release()

# With rlock this will not happend
lock = threading.RLock()
lock.acquire()
num += 3
print("num 3: ", num)
lock.acquire()
num += 4
print("num 4: ", num)
lock.release()
lock.release()