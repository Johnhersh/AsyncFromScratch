import threading
import queue
import random
import time

class Task:
    def __init__(self, func):
        self.func = func
        self.done_event = threading.Event()
        self.result = None

    def run(self):
        self.result = self.func()
        self.done_event.set()

    def wait(self):
        self.done_event.wait()
        return self.result

class ThreadPool:
    def __init__(self, num_workers):
        self.work_queue = queue.Queue()
        self.workers = []

        for _ in range(num_workers):
            worker = threading.Thread(target=self.worker_loop)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def queue_work(self, work):
        self.work_queue.put(work)

    def worker_loop(self):
        while True:
            task = self.work_queue.get()
            if task is None:
                break
            task.run()
            if task.result is not None:
                print(f"Worker {threading.current_thread().name} processed: {task.result}")
            self.work_queue.task_done()

    def run_all(self, tasks):
        for task in tasks:
            self.queue_work(task)
        for task in tasks:
            task.wait()

def work_function(i):
    time.sleep(random.randint(1, 500) / 1000)
    return f"message #{i}"

start_time = time.time()

thread_pool = ThreadPool(4)

tasks = [Task(lambda i=i: work_function(i)) for i in range(100)]

thread_pool.run_all(tasks)

end_time = time.time()
all_results = [task.result for task in tasks]

print(f"Total time taken: {end_time - start_time:.2f} seconds")
print(f"All results: {all_results}")