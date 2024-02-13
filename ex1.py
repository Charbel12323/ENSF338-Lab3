def merge_sort(arr,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)


def merge(arr, low, mid, high):
    length_l = mid - low + 1  
    length_r = high - mid 

    # Create temporary arrays
    left= [0] * length_l
    right= [0] * length_r

    for i in range(0, length_l):
        left[i] = arr[low + i]
    for j in range(0, length_r):
        right[j] = arr[mid + 1 + j]

    i = 0  
    j = 0  
    k = low  

    while i < length_l and j < length_r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    
    while i < length_l:
        arr[k] = left[i]
        i += 1
        k += 1

  
    while j < length_r:
        arr[k] = right[j]
        j += 1
        k += 1


a=[43, 72, 43, 73, 54, 5, 48, 26, 59, 73]

merge_sort(a,0,(len(a) -1))
print(a)


#2) The array is recursively split into two halves until subarrays of size 1 are left.Since each time we perform the split, we divide the array size by 2. Hence, the depth of the recursion tree is log n.The merging process requires comparing elements from both subarrays, which can take up to n comparisons in the worst case.Since there are log n levels (depth of the recursion) and at each level we perform O(n) work (to merge all elements at that level), the total work done is O(n log n).
