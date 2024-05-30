import threading
import time
import psutil

# Global shared counter and lock
shared_counter = 0
counter_lock = threading.Lock()

###############################################################################

def thread1_func(duration):
    global shared_counter
    start_time = time.time()
    while time.time() - start_time < duration:
        with counter_lock:
            if shared_counter % 2 == 0:
                shared_counter += 1

def thread2_func(duration):
    global shared_counter
    start_time = time.time()
    while time.time() - start_time < duration:
        with counter_lock:
            if shared_counter % 2 != 0:
                shared_counter += 1

###############################################################################

# Function to assign threads to specific CPUs and measure throughput
def assign_and_measure(cpu1, cpu2, duration=1):
    global shared_counter
    shared_counter = 0

    t1 = threading.Thread(target=thread1_func, args=(duration,))
    t2 = threading.Thread(target=thread2_func, args=(duration,))

    t1.start()
    t2.start()

    # Set CPU affinity for threads after they start
    psutil.Process(t1.native_id).cpu_affinity([cpu1])
    psutil.Process(t2.native_id).cpu_affinity([cpu2])

    t1.join()
    t2.join()

    return shared_counter / duration  # Throughput

###############################################################################

if __name__ == "__main__":

    # Main experiment: run for all CPU pairs and collect throughput data
    num_cpus = psutil.cpu_count(logical=False)  # Number of physical cores (false)
    # num of phys + virtual (True)

    print(num_cpus)

    for cpu1 in range(num_cpus):
        for cpu2 in range(num_cpus):

            print(assign_and_measure(cpu1, cpu2), end=" ")
        print()

###############################################################################
