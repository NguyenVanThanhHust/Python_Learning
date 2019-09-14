import threading 
import time

# create 2 thread for 2 task :
# 1st is to write a file in background
# 2nd is to create a string and save it to a file in a backgourn

class AsyncWrite(threading.Thread): # use threading.Thread as base class
	"""docstring for AsyncWrite"""
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text # self.text = text come in
		self.out = out
	def run(self):
		f = open(self.out, "a")
		f.write(self.text + '\n')
		f.close()
		time.sleep(2)
		print("Finished Background File Write to " + self.out)

def Main():
	message = input("Enter a string to store :")
	background = AsyncWrite(message, 'out.txt')
	background.start()
	print("The programm can continue while it writes in another thread")
	print("100 + 400 = ", 100 + 400)
	background.join() # wait for complete and continue
	print("waited until thread was complete")

if __name__ == '__main__':
	Main()
	
# main task is calculate 100 + 400 
# second task is write text in file
# it will finish the main task then go to second task
		