def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return comparisons, swaps

def run_bubble_sort_analysis(input_sizes):
    for size in input_sizes:
        input_array = list(range(size, 0, -1))  # Reverse ordered array
        comparisons, swaps = bubble_sort(input_array.copy())
        print(f"Input Size: {size}\tComparisons: {comparisons}\tSwaps: {swaps}")

# Example: Run the analysis on input sizes 10, 100, 1000
input_sizes = [10, 100, 1000]
run_bubble_sort_analysis(input_sizes)
