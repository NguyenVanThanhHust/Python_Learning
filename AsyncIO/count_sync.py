# This is synchronous version 
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.time()
    main()
    t = time.time()
    print("Time to take to process {}".format(t-s))