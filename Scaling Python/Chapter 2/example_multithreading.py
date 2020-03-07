import random
import threading
from timeit import default_timer as timer
results = []

def compute():
    results.append(sum([random.randint(1, 100) for i in range(10000)])) 

if __name__ == "__main__":
    start = timer()
    workers = [threading.Thread(target=compute) for x in range(8)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    
    print("results: ", results)
    end = timer()
    print(end-start)