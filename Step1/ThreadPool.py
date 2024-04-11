import threading
import queue
import random
import time

class ThreadPool:
    def __init__(self, num_workers):
        self.work_queue = queue.Queue()
        self.workers = []

        for _ in range(num_workers):
            worker = threading.Thread(target=self.worker_loop)
            worker.start()
            self.workers.append(worker)

    def queue_work(self, work_func):
        self.work_queue.put(work_func)

    def worker_loop(self):
        while True:
            work_func = self.work_queue.get()
            if work_func is None:
                break # Should be continue
            result = work_func()
            print(f"Worker {threading.current_thread().name} processed: {result}")
            self.work_queue.task_done() # Tell that *a* task is done, when the counter is 0 the pool can close via join
    
    def join(self): # Counts how many ongoing tasks are in the queue
        self.work_queue.join()
        for worker in self.workers:
            self.work_queue.put(None)
        for worker in self.workers:
            worker.join()

start_time = time.time()
thread_pool = ThreadPool(1)

def work_function(i):
    print(f"Running message {i}")
    time.sleep(random.randint(1, 100) / 1000)
    return i

for i in range(100):
    thread_pool.queue_work(lambda i=i: work_function(i))

thread_pool.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")