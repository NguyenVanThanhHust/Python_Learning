# https://medium.com/better-programming/synchronization-primitives-in-python-564f89fee732

# Semaphores are advanced counter. If we have threads that call to semaphore,
# this will be blocked after a number of thread had acquired it

import random, time
import threading
