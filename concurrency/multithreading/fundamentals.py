# 1. Create 3 threads and print names.
# 2. Demonstrate start() vs run().
# 3. Demonstrate join().
# 4. Demonstrate daemon thread.

from threading import Thread
import threading
import time

# 1. + # 3. -> Create 3 threads and print names and demonstrate join()
def print_thread_name(thread_id):
    print(f"Thread {thread_id} is starting.")
    time.sleep(1)  # Simulate some work
    print(f"Thread {thread_id} is running.")

threads = []

# first start all threads using start() method
for i in range(3):
    thread = Thread(target=print_thread_name, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

# Main program continues after all threads have completed
print("Main Program is running.")

# 2. Demonstrate start() vs run()
class WorkerThread(Thread):
    def run(self):
        print("current running thread name: ", threading.current_thread().name)

w = WorkerThread()
w.run()  # This will run in the main thread, not as a separate thread

w.start()  # This will run in a separate thread and this will also call the run() method

# 4. Demonstrate daemon thread.
def daemon_thread():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

daemon = Thread(target=daemon_thread, daemon=True)  # Set as daemon thread
daemon.start()

time.sleep(5) # Let the daemon thread run for a while before the main thread exits
print("Main thread exiting")