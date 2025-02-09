import random

"""
Partitions the array based on randomly chosen pivot.
param arr: The array to partition.
param l: The starting index of the subarray.
param r: The ending index of the subarray.
return: The index of the pivot after partitioning.
"""
def partation(arr, l, r):
    # get random pivot index
    pivot_index = random.randint(l, r)
    # move pivot element to the end
    arr[r], arr[pivot_index] = arr[pivot_index], arr[r]
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # moves the pivot to the correct position
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


"""
Finds the k-th smallest element in arr using Randomized Quickselect.
param arr: The array to search.
param l: The starting index of the subarray.
param h: The ending index of the subarray.
param k: The k-th smallest element to find (1-based index).
return: The k-th smallest element.
raises ValueError: If k is out of bounds (k > len(arr) or k <= 0).
"""
def randomized_quickselect(arr, l, r, k):
     # Handle invalid k values
    if k <= 0 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}. Got k = {k}.")
    
    # Base case: If the subarray has only one element, return it
    if l == r:
        return arr[l]
    # gets the partion index with partitioned array
    pivot = partation(arr, l, r)

    # recursively returns the kth smallest element if the k is smaller than pivot
    if k-1 < pivot:
        return randomized_quickselect(arr, l, pivot-1, k)
    # returns the pivot element if the kth samllest is pivot
    elif k-1 == pivot:
        return arr[pivot]
    # recursively returns the kth element from right part if the kth is grater than pivot
    else:
        return randomized_quickselect(arr, pivot+1, r, k)
        

arr = [3, 6, 2, 7, 5, 1, 4, 9, 8]
k = 4
try:
    result = randomized_quickselect(arr,0, len(arr)-1, k)
    print(f"The {k}-th smallest element is: {result}")
except ValueError as e:
    print(e)


