import random
import threading

# Number of nodes in the network
NUM_NODES = 5

# Initialize local values for each node
local_values = [random.randint(1, 100) for _ in range(NUM_NODES)]
global_average = 0

# Lock for synchronization
lock = threading.Lock()

# Function to compute the average of local values
def compute_local_average():
    with lock:
        local_average = sum(local_values) / len(local_values)
        print(f"Local average: {local_average}")
        return local_average

# Function to update global average using local averages
def update_global_average():
    global global_average
    threshold = 1e-6  # Convergence threshold
    while True:
        local_average = compute_local_average()
        with lock:
            global_average = (global_average + local_average) / 2
        print(f"Updated global average: {global_average}")
        if abs(global_average - local_average) < threshold:
            break

# Start a thread to continuously update the global average
update_thread = threading.Thread(target=update_global_average)
update_thread.start()

# Main thread waits for the update thread to finish
update_thread.join()

print(f"Final global average: {global_average}")
