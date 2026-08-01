from log_message import LogMessage
from backend import Backend
from queue import Queue
from threading import Event, Thread, Lock

class AsyncLogDispatcher:
    def __init__(self):
        self._queue = Queue(maxsize=1000) # backpressure to only get at max 1000 msgs

        # prepare a consumer thread to consume the messages from the queue and dispatch them to the backends
        self._consumer_thread = Thread(target=self._consume)
        self._consumer_thread.start()
        self._submit_lock = Lock()
        self._stop_event = Event() # thread-safe boolean to restrict submit if stop() has been called
        
    def submit(self, message: LogMessage, backends: list[Backend]):
        # check if stop() has been called, if so, raise an exception
        with self._submit_lock:
            if self._stop_event.is_set():
                raise RuntimeError("Cannot submit messages after stop() has been called.")
            self._queue.put((message, backends))
    
    def _consume(self):
        while True:
            job = self._queue.get() # this gets hold on empty queue to avoid busy waiting
            # sentinel value to stop the consumer thread
            if job is None:
                self._queue.task_done()
                break
            # process the job
            message, backends = job
            for backend in backends:
                try:
                    backend._write(message)
                except Exception as e:
                    print(f"Failed to write logs to backend {backend}, exception: {e}")
            # mark the job as done
            self._queue.task_done()

    def stop(self):
        with self._submit_lock:
            self._stop_event.set() # set the stop event to prevent further submissions
        self._queue.join() # wait for all the jobs to be processed
        self._queue.put(None) # put a sentinel value to stop the consumer thread
        self._consumer_thread.join(timeout=5) # wait for the consumer thread to finish at most 5 seconds
        if self._consumer_thread.is_alive():
            print("Consumer thread is still alive after stop() call, something went wrong.")