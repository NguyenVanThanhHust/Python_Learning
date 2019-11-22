# https://medium.com/better-programming/synchronization-primitives-in-python-564f89fee732

from threading import Lock, Thread
lock = Lock()
g = 0

def add_one():
    """
    Demonstatration purpose only. Global is bad
    """
    global g
    lock.acquire()
    g += 1
    lock.release()

def add_two():
    """
    Demonstatration purpose only. Global is bad
    """
    global g
    lock.acquire()
    g += 2
    lock.release()

threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()

print(g)