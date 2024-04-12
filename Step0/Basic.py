import random
import time

start_time = time.time()

def work_function(i):
    print(f"Handling request {i}")
    time.sleep(random.randint(1, 100) / 1000)
    return i

for i in range(100):
    work_function(i)

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")