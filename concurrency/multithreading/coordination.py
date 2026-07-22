# 1. Basic queue implementation
from queue import Queue
from threading import Thread
import time

email_send_queue = Queue(maxsize=1000) # queue creation with backpressure setting

def worker():
    while True:
        email = email_send_queue.get()
        print(f"sending email to {email}")
        time.sleep(1)
        print("email sent")
        email_send_queue.task_done()

Thread(target=worker,daemon=True).start() # will run worker until all non-daemon thread is working
# Note if daemon=False then worker will run forever and this is useful in some cases

# producer which add task to queue
def register_user(user):
    print("add user to db")
    email_send_queue.put(user)

register_user("kumarnitesh2000.nk@gmail.com")
register_user("kumaranmol.ak2001@gmail.com")

email_send_queue.join() # now this will make sure that all threads of email sending completes 
print("All emails sent")

# 2. Event
from threading import Event

event = Event()
def worker():
    print("waiting for model to load")
    event.wait() # this will block the thread and will not run until the event is set
    print("worker is working..")

th = Thread(target=worker)
th.start()
time.sleep(2) # loading model
event.set() # setting after all pre-requisite tasks done
th.join()

# 3. Barrier - Commonly used in map-reduce
from threading import Barrier

barrier = Barrier(parties=3) # here parties means how many party to wait for before opening the barrier

def worker(id):
    print(f"thread-{id} entered phase1")
    print("waiting for barrier")
    barrier.wait()
    print(f"thread-{id} entered phase2")

threads = []
num = 2 # this will never open barrier because 2 < 3
num = 3
for idx in range(3):
    th = Thread(target=worker,args=(idx,))
    threads.append(th)
    th.start()

for th in threads:
    th.join()

# 4. Common co-ordination problems
    ## problem 1. if we don't have anything in our queue my consumer is continously running and consuming CPU so we need to block that thread.
    ## problem 2. if producer is much faster then consumer at that time we have to block producer so that consumer process the task.

# so for problem 1 we will be using queue.get which will wait if no tasks and backpressure setting blocks producer if maxsize is finished.