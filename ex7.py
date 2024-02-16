import json
import time
import matplotlib.pyplot as plt

# Standard binary search function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Read array data from ex7data.json
with open('ex7data.json', 'r') as file:
    array = json.load(file)

# Read search tasks from ex7tasks.json
with open('ex7tasks.json', 'r') as file:
    search_tasks = json.load(file)

task_numbers = []
best_midpoints = []

# Set the step size for midpoints
step_size = 10

# Perform binary search for each task with different midpoints and choose the best one
for target in search_tasks:
    if isinstance(target, int):
        best_midpoint = 0
        best_time = float('inf')

        # Try different midpoints with a step size
        for midpoint in range(0, len(array), step_size):
            start_time = time.time()
            found = binary_search(array, target)
            end_time = time.time()
            elapsed_time = end_time - start_time

            if found and elapsed_time < best_time:
                best_time = elapsed_time
                best_midpoint = midpoint

        task_numbers.append(target)
        best_midpoints.append(best_midpoint)

# Plot scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(task_numbers, best_midpoints, color='blue', marker='o', s=50)
plt.title('Chosen Midpoints for Search Tasks')
plt.xlabel('Task Numbers')
plt.ylabel('Chosen Midpoint')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
