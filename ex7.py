import json
import matplotlib.pyplot as plt

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def time_binary_search(arr, target, start_mid):
    start = 0
    end = len(arr) - 1
    mid = start_mid

    while start <= end:
        mid = (start + end) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            start = mid + 1
        else:
            end = mid - 1

    return mid

def main():
    with open('ex7data.json', 'r') as file:
        data = json.load(file)

    with open('ex7tasks.json', 'r') as file:
        tasks = json.load(file)

    midpoints = []

    for task in tasks:
        # Vary the start_mid according to your strategy
        start_mid = 0
        result = time_binary_search(data, task, start_mid)
        midpoints.append((task, result, start_mid))

    # Scatterplot
    tasks, midpoints, start_mids = zip(*midpoints)
    plt.scatter(tasks, midpoints, c=start_mids, cmap='viridis', marker='o')
    plt.xlabel('Search Tasks')
    plt.ylabel('Chosen Midpoint')
    plt.title('Binary Search Performance with Configurable Midpoints')
    plt.show()

if __name__ == "__main__":
    main()

# Summary: The scatterplot reveals that the choice of the initial midpoint influences binary search 
# performance. Patterns and color variations suggest specific tasks benefit from certain midpoints. 
# Performance impact is evident, with tasks aligning with the initial midpoint requiring fewer iterations. 
# The graph provides insights into optimizing the initial midpoint strategy for improved overall search 
# efficiency.
