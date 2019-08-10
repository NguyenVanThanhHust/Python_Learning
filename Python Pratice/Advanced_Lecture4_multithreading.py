# this is learn about multithreading in python
# thread is a part of program running along side each other
# but they can share data because in run within one process

from threading import Thread
import time

def timer(name, delay, repeat):
	print("Timer: " + name + "Started")
	while repeat > 0:
		time.sleep(delay)
		print(name + ": " + str(time.ctime(time.time())))
		repeat -= 1
	print("Timer: " + name + " is finished")

def Main():
	# Create new thread
	t1 = Thread(target = timer, args = ("Timer1", 1, 5))
	t2 = Thread(target = timer, args = ("Timer2", 2, 5))
	t1.start()
	t2.start()
	print("Main completed")

if __name__ == '__main__':
	Main()
