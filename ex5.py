
import time
import random
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, val, start, end):
    
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
     
        j = binary_search(arr, key, 0, i - 1)
      
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr


def generate_random_arrays(lengths):
    return [[random.randint(0, 1000) for _ in range(length)] for length in lengths]

array_lengths = [100, 200, 500, 1000, 2000,5000]

test_arrays = generate_random_arrays(array_lengths)

execution_times = {
    'traditional_insertion_sort': [],
    'binary_insertion_sort': []
}

for arr in test_arrays:
    start_time = time.time()
    insertion_sort(arr.copy())
    execution_times['traditional_insertion_sort'].append(time.time() - start_time)
    
for arr in test_arrays:
    start_time = time.time()
    binary_insertion_sort(arr.copy())  # Use a copy to keep the original array unchanged
    execution_times['binary_insertion_sort'].append(time.time() - start_time)

print(execution_times)


x_fine = np.linspace(min(array_lengths), max(array_lengths), 300)

f_traditional = interp1d(array_lengths, execution_times['traditional_insertion_sort'], kind='cubic')
f_binary = interp1d(array_lengths, execution_times['binary_insertion_sort'], kind='cubic')


y_traditional_fine = f_traditional(x_fine)
y_binary_fine = f_binary(x_fine)


plt.figure(figsize=(10,6))
plt.plot(array_lengths, execution_times['traditional_insertion_sort'], 'o', label='Traditional Insertion Sort')
plt.plot(x_fine, y_traditional_fine, '-', label='Traditional Sort Interpolated')
plt.plot(array_lengths, execution_times['binary_insertion_sort'], 's', label='Binary Insertion Sort')
plt.plot(x_fine, y_binary_fine, '--', label='Binary Sort Interpolated')
plt.title('Execution Time of Insertion Sort Algorithms with Interpolating Functions')
plt.xlabel('Array Length')
plt.xlabel('Array Length')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()


#4)  Between the two sorting methods tested, the binary insertion sort is generally quicker than the traditional insertion sort and thats becuase in insertion sort we have to put the item in the right spot  so we have to compare it with many other items one by one so that would take a long time.
# However, Binary insertion sort is faster in locating where to put the item as it uses binarhy search therefore that is why its faster.