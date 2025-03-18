import time
import random
from pyinstrument import Profiler

# Example script to demonstrate pyinstrument profiling


def cpu_intensive_task():
    """A function that does some CPU-intensive work."""
    data = [random.random() for _ in range(1000000)]
    data.sort()
    return sum(data)

def io_simulation():
    """A function that simulates I/O operations."""
    time.sleep(0.5)  # Simulate I/O delay
    return "I/O operation completed"

def mixed_task():
    """A function that mixes CPU and I/O operations."""
    result1 = cpu_intensive_task()
    result2 = io_simulation()
    return result1, result2

def main():
    # Create a profiler
    profiler = Profiler()

    # Start profiling
    profiler.start()

    # Run the code you want to profile
    result = mixed_task()
    print(f"Task completed with result: {result[0]:.2f}, {result[1]}")

    # Stop profiling
    profiler.stop()

    # Print the results
    print("\nProfiling Results:")
    print(profiler.output_text(unicode=True, color=True))

if __name__ == "__main__":
    main()
