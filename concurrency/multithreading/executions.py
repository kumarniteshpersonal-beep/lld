# In real-world to execute the tasks we will be using ThreadPoolExecutor because we can create thread for each req
from concurrent.futures import ThreadPoolExecutor,as_completed
import time

def squares(num):
    time.sleep(1/num)
    return num*num

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    # 12 tasks are there but at max 3 workers / thread will be created
    for idx in range(12):
        futures.append(executor.submit(squares,idx))
    
    # use as-completed to process the result whenever they are ready
    for future in as_completed(futures):
        # note future can consist of result or exception
        try:
            print(future.result())
        except ZeroDivisionError as e:
            print(future.exception())