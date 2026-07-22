# Race Condition - Updating shared state by multiple threads without proper synchronization can lead to inconsistent or unexpected results. This will effect the correctness of the program.
# Common Examples occus in check-then-act and read-modify-write operations. and both of these operations are not atomic.

# Example of incorrectness
from threading import Thread
import threading,time

counter =  0
def work():
    global counter
    for _ in range(100):
        temp = counter
        time.sleep(0.001)
        counter = temp + 1

threads = []
for idx in range(10):
    th = Thread(target=work)
    threads.append(th)
    th.start()

for th in threads:
    th.join()

print(f"Final counter value is {counter} and expected value is 1000")

# How to correct this
counter =  0
lock = threading.Lock()
def work():
    global counter
    for _ in range(100):
        with lock:
            temp = counter
            time.sleep(0.001)
            counter = temp + 1

threads = []
for idx in range(10):
    th = Thread(target=work)
    threads.append(th)
    th.start()

for th in threads:
    th.join()

print(f"Final counter value is {counter} and expected value is 1000")

# Nested Locking Issue
counter1,counter2 =  0,0
# lock = threading.Lock()
lock = threading.RLock() # in nested lock case Rlock can help because it has reference of owner thread
def work():
    global counter1,counter2
    for _ in range(100):
        # nested locks
        with lock: # parent section
            counter1+=1
            with lock:# child section
                counter2+=1
# funny part while child section is trying to acquire lock in that situation lock instance thinks that some another thread is requesting this.
# so this locks does't know anout parent threead hence this is deadlock.

threads = []
for idx in range(10):
    th = Thread(target=work)
    threads.append(th)
    th.start()

for th in threads:
    th.join()

print("I am reaching here because I am using RLock!")

# Note if there are more then one lock in that case acquire lock in fixed order and all threads should follow those.