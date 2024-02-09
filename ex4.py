import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage
input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quicksort(input_array)
print("Sorted array:", sorted_array)

# Worst-case scenario
worst_case_input = list(range(1, 10001))

start_time = time.time()
quicksort(worst_case_input)
end_time = time.time()

execution_time = end_time - start_time
print(f"Time taken to sort worst-case input: {execution_time} seconds")
