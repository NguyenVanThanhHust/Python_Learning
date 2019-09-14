import multiprocessing
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
		process1 = multiprocessing.Process(target = m_function, args = (number, ))
		# process2 = multiprocessing.Process(target = m_function, args = (number, ))
		# process3 = multiprocessing.Process(target = m_function, args = (number, ))
		# process4 = multiprocessing.Process(target = m_function, args = (number, ))
		process1.start()
		# process2.start()
		# process3.start()
		# process4.start()
		process1.join()
		# process2.join()
		# process3.join()
		# process4.join()
		end = time.time()
		each_execution_time = end - start
		execution_time.append(each_execution_time)
	print("Execution time: ", sum(execution_time)/len(execution_time))

if __name__ == '__main__':
	main()
	"""
	1 process : Execution time: 0.4770755238003201
	2 process : Execution time: 0.44362632433573407
	3 process : Execution time: 0.6393444273206923
	4 process : Execution time: 0.5610156059265137
	"""
