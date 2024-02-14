import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_performance(algorithm, input_size):
    arr = list(range(input_size))
    random.shuffle(arr)
    target = random.choice(arr)

    start_time = time.time()
    result = algorithm(arr, target)
    end_time = time.time()

    return end_time - start_time

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_search_times = []
binary_search_times = []

for size in input_sizes:
    linear_time = measure_performance(linear_search, size)
    binary_time = measure_performance(binary_search, size)

    linear_search_times.append(linear_time)
    binary_search_times.append(binary_time)


plt.plot(input_sizes, linear_search_times, label='Linear Search')
plt.plot(input_sizes, binary_search_times, label='Binary Search')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Algorithm Performance Comparison')
plt.legend()
plt.show()

# 4. Discussing the results
# You can analyze the plot and discuss which algorithm is faster for different input sizes.
# For smaller input sizes, linear search might be faster due to its simplicity.
# Binary search may become more efficient as the input size increases, especially for sorted arrays.
