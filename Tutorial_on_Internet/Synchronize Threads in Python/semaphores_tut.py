# https://medium.com/better-programming/synchronization-primitives-in-python-564f89fee732

# Semaphores are advanced counter. If we have threads that call to semaphore,
# this will be blocked after a number of thread had acquired it

import random, time
import threading
from threading import BoundedSemaphore, Thread

max_items = 5

container = BoundedSemaphore(max_items)
def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produced an item")
        except ValueError:
            print("Full, skipping")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        if container.acquire(False):
            print("Consumed an item")
        else:
            print("Empty, skipping")
        
threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))
for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")