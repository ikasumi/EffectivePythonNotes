from threading import Thread
from time import sleep
import random

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # 何らかの処理
        sleep(random.uniform(0, 1e-7))
        counter.increment(1)

def run_thread(func, how_many, counter, num_thread=5):
    threads = []
    for i in range(num_thread):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for i in threads:
        thread.join()

# Counter should be 5000, found 5000
# Counter should be 5000, found 4979
# Counter should be 5000, found 4987
# += 演算の途中であるThreadの演算が停止して、ほかのThreadが演算するために起きる

how_many = 10**3
num_thread = 5
counter = Counter()
run_thread(worker, how_many, counter, num_thread)
print("Counter should be %d, found %d" % (num_thread * how_many, counter.count))

how_many = 10**2
num_thread = 50
counter = Counter()
run_thread(worker, how_many, counter, num_thread)
print("Counter should be %d, found %d" % (num_thread * how_many, counter.count))

how_many = 10**1
num_thread = 500
counter = Counter()
run_thread(worker, how_many, counter, num_thread)
print("Counter should be %d, found %d" % (num_thread * how_many, counter.count))
