import time
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.time()
    asyncio.run(main())
    t = time.time()
    print("Time to take to process {}".format(t-s))