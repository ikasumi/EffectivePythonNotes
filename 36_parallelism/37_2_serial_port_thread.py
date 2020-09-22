import time
import select, socket
from threading import Thread

def slow_systemcall():
    # システムに0.1秒のブロッキングを要求してからプログラムに制御を戻す
    select.select([socket.socket()], [], [], 0.1)

# serial 
start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print("Took %.3f seconds with serial processing." % (end - start))

# Thread 
# 処理は増えているのに、所要時間は、直列処理の1回 0.05s の処理がボトルネックに移動する
start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def complicated_time_consuming_compute():
    time.sleep(0.05)

for i in range(5):
    complicated_time_consuming_compute()
for thread in threads:
    thread.join()
end = time.time()
print("Took %.3f seconds with Thread processing." % (end - start))
