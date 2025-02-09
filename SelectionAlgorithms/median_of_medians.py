# arr is the array from where kth smallest element is to be selected
# kth smallest element k starts from 0
def median_of_medians(arr, k):
    # returns kth element from sorted arr if arr size is 5 or less 
    if len(arr) <= 5:
        return sorted(arr)[k]
    # arr_size_5 contains sub array of size 5 of the original array
    arr_size_5 = [arr[i:i+5] for i in range(0, len(arr), 5)]
    # contains median from sorted size 5 array 
    medians = [sorted(ar)[len(ar)//2] for ar in arr_size_5]

    # recurssively gets the median of medians
    pivot = median_of_medians(medians, len(medians)//2)

    # slices the array into left and right based on pivot
    left = [x for x in arr if x < pivot]
    # middle contains pivot elements 
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # if the kth element is on the left recursively get kth element
    if k < len(left):
        return median_of_medians(left, k)
    # if in in middle array simply returns pivot
    elif k < (len(left) + len(middle)):
        return pivot
    # if on right recursively return kth of original array but (kth -left array - middle array of right array)
    else:
        return median_of_medians(right, k - len(left) - len(middle))
    

arr = [3, 6, 2, 7, 5, 1, 4, 9, 8]
k = 4
try:
    result = median_of_medians(arr, k-1)
    print(f"The {k}-th smallest element is: {result}")
except ValueError as e:
    print(e)
