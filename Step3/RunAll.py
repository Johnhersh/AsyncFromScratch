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
        self.thread_pool.queue_work(self)
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

    def queue_work(self, work_func):
        self.work_queue.put(work_func)

    def worker_loop(self):
        while True:
            task = self.work_queue.get()
            if task is None:
                continue
            task.run()
            print(f"Worker {threading.current_thread().name} processed: {task.result}")
    
    def run_all(self, tasks):
        for task in tasks:
            self.queue_work(task)
        for task in tasks:
            task.wait()

start_time = time.time()
thread_pool = ThreadPool(1)

def work_function(i):
    print(f"Handling request {i}")
    time.sleep(random.randint(1, 100) / 1000)
    return i

# Create tasks without queuing them, similar to Promise.all() in js
tasks = [Task(lambda i=i: work_function(i), thread_pool) for i in range(100)]

# Wait for all tasks to complete; they get queued upon calling wait()
thread_pool.run_all(tasks)

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")