import threading
import queue
import random
import time

class Task:
    def __init__(self, func, thread_pool):
        self.func = func
        self.done_event = threading.Event()
        self.result = None
        self.thread_pool = thread_pool
        # Note: We should also save the exception, but f it

    def run(self):
        self.result = self.func()
        self.done_event.set()

    def wait(self):
        self.thread_pool.queue_work(self.run)
        self.done_event.wait()
        return self.result

class ThreadPool:
    def __init__(self, num_workers):
        self.work_queue = queue.Queue()
        self.workers = []

        for _ in range(num_workers):
            worker = threading.Thread(target=self.worker_loop)
            worker.daemon = True  # Daemon threads will exit when the main program exits
            worker.start()
            self.workers.append(worker)

    def queue_work(self, work):
        self.work_queue.put(work)

    def worker_loop(self):
        while True:
            work = self.work_queue.get()
            if work is None:
                return
            work()
            self.work_queue.task_done() # Tell that *a* task is done, when the counter is 0 the pool can close via join

    def join(self):
        self.work_queue.join()  # Wait for all tasks to be processed


start_time = time.time()
thread_pool = ThreadPool(4)

def work_function(i):
    print(f"Processing message {i}")
    time.sleep(random.randint(1, 1000) / 1000)
    return i

# Create tasks without queuing them
tasks = [Task(lambda i=i: work_function(i), thread_pool) for i in range(100)]

# Wait for each task to complete; they get queued upon calling wait()
for task in tasks:
    result = task.wait()  # This will execute them one at a time
    print(f"Task result: {result}")

# No need to join the threads if they are daemons, as they will exit with the main program
# If you want to ensure they finish even if the main program can exit, uncomment the next line
# thread_pool.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")