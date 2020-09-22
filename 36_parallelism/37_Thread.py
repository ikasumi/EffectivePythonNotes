import time
from threading import Thread

def factorize(number):
    for i in range(1, number+1):
        if number %i == 0:
            yield i

numbers = [213979, 1214759, 1516637, 1852285]
# numbers = [213979, 1214759, 1516637, 1852285, 213979, 1214759, 1516637, 1852285,213979, 1214759, 1516637, 1852285,213979, 1214759, 1516637, 1852285]

# 直列
start = time.time()
for number in numbers:
    print(list(factorize(number)))
end = time.time()
print("Took %.3f seconds straight." % (end - start))

# Thread ※GILのせいで同時に1スレッドしか実行できないので早くならない
# Thread は Blocking I/O （ネットワークやディスクなど）を回避するために使わないと意味がない
class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))
        print(self.factors)

start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print("Took %.3f seconds with using Thread." % (end - start))
