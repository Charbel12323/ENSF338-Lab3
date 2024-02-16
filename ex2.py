import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    # Bubble Sort implementation
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    # Quick Sort implementation
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size):
    # Generate a random array of given size
    return [random.randint(1, 100) for _ in range(size)]

def test_algorithm(algorithm, case, size):
    # Test the algorithm on a given case and return the execution time
    arr = generate_random_array(size)
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{algorithm.__name__} - {case} case - Size: {size} - Time: {execution_time:.6f} seconds")
    return execution_time

def plot_performance_sizes(sizes, algorithm1_times, algorithm2_times, algorithm1_name, algorithm2_name):
    # Plot performance for different input sizes
    plt.plot(sizes, algorithm1_times, label=f"{algorithm1_name}")
    plt.plot(sizes, algorithm2_times, label=f"{algorithm2_name}")
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'{algorithm1_name} vs {algorithm2_name} - Performance Comparison')
    plt.legend()
    plt.show()

# Specify input sizes
sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 200, 240, 280, 320, 400, 500, 700]

# Test algorithms on best, worst, and average cases
best_case_times_bubble = [test_algorithm(bubble_sort, "best", size) for size in sizes]
worst_case_times_bubble = [test_algorithm(bubble_sort, "worst", size) for size in sizes]
average_case_times_bubble = [test_algorithm(bubble_sort, "average", size) for size in sizes]

best_case_times_quick = [test_algorithm(quick_sort, "best", size) for size in sizes]
worst_case_times_quick = [test_algorithm(quick_sort, "worst", size) for size in sizes]
average_case_times_quick = [test_algorithm(quick_sort, "average", size) for size in sizes]

# Plot performance for each case
plot_performance_sizes(sizes, best_case_times_bubble, best_case_times_quick, "Best Case Bubble Sort", "Best Case Quick Sort")
plot_performance_sizes(sizes, worst_case_times_bubble, worst_case_times_quick, "Worst Case Bubble Sort", "Worst Case Quick Sort")
plot_performance_sizes(sizes, average_case_times_bubble, average_case_times_quick, "Average Case Bubble Sort", "Average Case Quick Sort")
