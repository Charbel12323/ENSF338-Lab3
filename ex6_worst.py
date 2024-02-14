import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def measure_performance(algorithm, input_size):
    arr = list(range(input_size))
    random.shuffle(arr)  # Shuffle the array to make it random
    target = random.choice(arr)

    start_time = time.time()
    result = algorithm(arr)
    end_time = time.time()

    return end_time - start_time

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

quicksort_times = []

for size in input_sizes:
    quicksort_time = measure_performance(quicksort, size)
    quicksort_times.append(quicksort_time)


plt.plot(input_sizes, quicksort_times, label='Quicksort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Quicksort Worst-Case Performance')
plt.legend()
plt.show()

# 5. Discuss the results
# Analyze the plot and discuss how Quicksort's 
# performance deteriorates as the input size 
# increases, especially for already sorted arrays.
