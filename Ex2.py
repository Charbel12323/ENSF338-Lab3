import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def test_algorithm(algorithm, size):
    arr = generate_random_array(size)
    start_time = time.time()
    sorted_arr = algorithm(arr)
    end_time = time.time()
    return end_time - start_time


sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
bubble_times = []
quick_times = []

for size in sizes:
    bubble_time = test_algorithm(bubble_sort, size)
    quick_time = test_algorithm(quick_sort, size)
    bubble_times.append(bubble_time)
    quick_times.append(quick_time)

print(bubble_times)
print(quick_times)
