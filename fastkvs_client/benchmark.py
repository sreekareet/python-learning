import threading
import time
import queue
from client import FastKVSClient
from exceptions import FastKVSError

def worker(thread_id, num_ops, results_queue):
    latencies = []
    
    try:
        with FastKVSClient("127.0.0.1", 7379) as client:
            for i in range(num_ops):
                key = f"bench:thread{thread_id}:key{i}"
                value = f"value{i}"
                
                start = time.perf_counter()
                client.set(key, value)
                client.get(key)
                end = time.perf_counter()
                
                latencies.append((end - start) * 1000)  # convert to ms
                
        results_queue.put({"thread_id": thread_id, "latencies": latencies, "error": None})
    
    except FastKVSError as e:
        results_queue.put({"thread_id": thread_id, "latencies": [], "error": str(e)})

def run_benchmark(num_threads=3, num_ops=10):
    print(f"\n=== FastKVS Benchmark ===")
    print(f"threads: {num_threads}, ops per thread: {num_ops}")
    print(f"total operations: {num_threads * num_ops * 2} (SET+GET pairs)\n")
    
    results_queue = queue.Queue()
    threads = []
    
    start = time.perf_counter()
    
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i, num_ops, results_queue))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    total_time = (time.perf_counter() - start) * 1000

    all_latencies = []
    for _ in range(num_threads):
        result = results_queue.get()
        if result["error"]:
            print(f"thread {result['thread_id']} failed: {result['error']}")
        else:
            all_latencies.extend(result["latencies"])
    
    if all_latencies:
        all_latencies.sort()
        total = len(all_latencies)
        print(f"total time:     {total_time:.1f}ms")
        print(f"operations:     {total}")
        print(f"min latency:    {min(all_latencies):.2f}ms")
        print(f"max latency:    {max(all_latencies):.2f}ms")
        print(f"avg latency:    {sum(all_latencies)/total:.2f}ms")
        print(f"p50 latency:    {all_latencies[int(total*0.50)]:.2f}ms")
        print(f"p99 latency:    {all_latencies[int(total*0.99)]:.2f}ms")

if __name__ == "__main__":
    run_benchmark(num_threads=10, num_ops=100)