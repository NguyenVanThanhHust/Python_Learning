import threading
import random
from functools import reduce
import time

def m_function(number):
	random_list = random.sample(range(100000), number)
	return reduce(lambda x, y: x* y, random_list)

number = 50000

def main():
	execution_time = list()
	for i in range(1,10):
		start = time.time()
		thread1 = threading.Thread(target = m_function, args = (number, ))
		thread2 = threading.Thread(target = m_function, args = (number, ))
		# thread3 = threading.Thread(target = m_function, args = (number, ))
		# thread4 = threading.Thread(target = m_function, args = (number, ))
		thread1.start()
		thread2.start()
		# thread3.start()
		# thread4.start()
		thread1.join()
		thread2.join()
		# thread3.join()
		# thread4.join()
		end = time.time()
		each_execution_time = end - start
		execution_time.append(each_execution_time)
	print("Execution time: ", sum(execution_time)/len(execution_time))

if __name__ == '__main__':
	main()
	"""
	Execution time:  
	1 thread = Execution time:  0.27678561210632324
	2 thread = Execution time:  1.37656659550137
	3 thread = Execution time:  1.7327411704593234
	4 thread = Execution time:  0.6223957538604736

	"""
