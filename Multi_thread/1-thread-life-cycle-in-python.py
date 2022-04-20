import os
import threading
import time 


# custom function 
def task(step=3):
    for i in range(step):
        print("i : {}".format(i))
        time.sleep(2)

# Create new thread
thread = threading.Thread(target=task, args=(5))

if thread.is_alive():
    thread.start()
else:
    thread.stop()