import random
from concurrent import futures
from timeit import default_timer as timer
results = []

def compute():
    return sum([random.randint(1, 100) for i in range(10000)])

if __name__ == "__main__":
    start = timer()
    with futures.ThreadPoolExecutor(max_workers=8) as executor:
        futs = [executor.submit(compute) for _ in range(8)]
    results = [f.result() for f in futs]
    
    print("results: ", results)
    end = timer()
    print(end-start)