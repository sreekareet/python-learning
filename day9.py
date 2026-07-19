import threading
import time

results = []

def fetch_from_server(thread_id):
    time.sleep(0.1) #simulate waiting for socket response - GIL released here
    results.append(f"thread {thread_id} done")

threads = []
start_time = time.time()
for i in range(5):
    thread = threading.Thread(target=fetch_from_server, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"time taken: {end_time - start_time:.2f} seconds")
print(results)

import threading
import time

def cpu_work():
    count = 0
    for i in range(5_000_000):
        count += i
    return count

# single threaded
start = time.time()
cpu_work()
cpu_work()
end = time.time()
print(f"sequential: {end - start:.2f}s")

# two threads
start = time.time()
t1 = threading.Thread(target=cpu_work)
t2 = threading.Thread(target=cpu_work)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"threaded: {end - start:.2f}s")

import threading

counter = 0
lock = threading.Lock() #prevents race condition

def increment():
    global counter
    for _ in range(100000):
        with lock:          # same with statement you know from file IO
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print(f"expected: 200000, got: {counter}")