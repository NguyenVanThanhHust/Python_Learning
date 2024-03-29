import time 
import asyncio
import itertools as it
import os
import random

async def makeitem(size: int=5) -> str:
    return os.urandom(size).hex()

async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n): # Synchronous loop for each single process
        await randsleep(caller=f"Producer {name}")
        i = await  makeitem()
        start_time = time.time()
        await q.put((i, start_time))
        print(f"Producer {name} added <{i}> to queue.")

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, st = await q.get()
        now = time.time()
        print((f"Consumer {name} got elemtn <{i}>"
                f" in {now - st:0.5f} seconds."))
        q.task_done()

            
async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()

    
if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start_time = time.time()
    asyncio.run(main(**ns.__dict__))
    end_time = time.time()
    print(f"Program complete in {end_time-start_time:0.5f} seconds")
    
    