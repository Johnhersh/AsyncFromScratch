import time
import random
import queue

class Task:
    def __init__(self, coroutine):
        self.coroutine = coroutine
        self.result = None
        self.done = False

    def step(self):
        try:
            # Assume that 'yield' is always used to wait for a certain amount of time
            wait_time = next(self.coroutine)
            scheduler.add_task(self, time.time() + wait_time)
        except StopIteration as e:
            self.result = e.value
            self.done = True

class Scheduler:
    def __init__(self):
        self.tasks = queue.PriorityQueue()

    def add_task(self, task, wake_time):
        self.tasks.put((wake_time, task))

    def run(self):
        while not self.tasks.empty():
            wake_time, task = self.tasks.get()
            now = time.time()
            if now < wake_time:
                time.sleep(wake_time - now)
            task.step()

# Define a simple coroutine using a generator
def coroutine_function(i):
    total_wait_time = random.randint(1, 100) / 1000  # Total wait time for the coroutine
    steps = random.randint(2, 5)  # Random number of steps
    print(f"Coroutine {i} will run for a total of {total_wait_time:.3f} seconds in {steps} steps.")

    for step in range(steps):
        yield_time = total_wait_time / steps  # Spend an equal fraction of time in each step
        print(f"Coroutine {i} step {step + 1}/{steps}, yielding for {yield_time:.3f} seconds")
        yield yield_time  # Yield control back to the scheduler, simulating an async wait

    print(f"Coroutine {i} completed")
    return i

def bad_coroutine_function():
    while True:
        pass
    return

# Create a scheduler
scheduler = Scheduler()

# Create tasks (coroutines) and add them to the scheduler
tasks = [Task(coroutine_function(i)) for i in range(100)]
tasks.append(bad_coroutine_function())
for task in tasks:
    scheduler.add_task(task, time.time())

# Run the scheduler
start_time = time.time()
scheduler.run()
end_time = time.time()

# Print results
for i, task in enumerate(tasks):
    print(f"Coroutine {i} result: {task.result}")

print(f"Total time taken: {end_time - start_time:.2f} seconds")