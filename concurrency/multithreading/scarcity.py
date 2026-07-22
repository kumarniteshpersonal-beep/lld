# Problem is that resource is limited and we want that only N concurrent threads will enter into section where we are using resources
# Lock can't help because it will only allow one thread to enter into that section.

from threading import Semaphore,Thread
import time

semaphore = Semaphore(3) # only 3 concurrent req allowed at a time

def work(idx):
    with semaphore:
        print(f"Fetching Data from DB for query, select * from x where id={idx}")
        time.sleep(1)
        print(f"Done fetching data for id={idx}")

# creating 10 threads to fetch data from db by id
threads = []
for idx in range(10):
    th = Thread(target=work,args=(idx,))
    threads.append(th)
    th.start()

for th in threads:
    th.join()