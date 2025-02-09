import sys
import numpy as np
import time
import matplotlib.pyplot as plt 
from median_of_medians import median_of_medians
from randomized_quickselect import randomized_quickselect

def time_to_find_kth_smallest(k=420, limit=1000000, np_arr_type="unsorted", search_algo="median_of_medians"):
    i = 1000
    timetaken = []
    while i < limit:
         # for random array
        array_list = np.random.randint(1, i*2, i).tolist()
        #to get sorted numpy array
        if np_arr_type == "reverse_sorted":
            array_list = np.arange(i, 0, -1).tolist()
        #to get reverse sorted numpy array
        elif np_arr_type == "sorted":
            array_list = np.arange(1, i+1).tolist()
        # call median_of_medians
        print(f"\nFinding {k}th smallest on {np_arr_type} array of size {i} using {search_algo}")
        result = -1
        tt = -1
        if search_algo == "median_of_medians":
            t1 = time.time()
            result = median_of_medians(array_list, k-1)
            tt = time.time()-t1
            timetaken.append(tt)
        # call randomized_quickselect
        else:
            t1 = time.time()
            result = randomized_quickselect(array_list, 0, len(array_list)-1, k)
            tt = time.time()-t1
            timetaken.append(tt)

        print(f"Time taken to find {k}th smallest element {result} is {tt}")
        i *= 2
    return timetaken


if __name__ == "__main__":

    # increase system recurssion depth to 1M
    sys.setrecursionlimit(100000)

    limit = 10000000
    k = 420

    arr_size = []
    i = 1000
    while i < limit:
        arr_size.append(i)
        i *= 2

    ###############################
    # median_of_medians
    ###############################
    unsorted_time_median_of_medians = time_to_find_kth_smallest(k, limit, "unsorted", "median_of_medians")
    sorted_time_median_of_medians = time_to_find_kth_smallest(k, limit, "sorted", "median_of_medians")
    r_sorted_time_median_of_medians = time_to_find_kth_smallest(k, limit, "reverse_sorted", "median_of_medians")

    ###############################
    # randomized_quickselect
    ###############################
    unsorted_time_randomized_quickselect = time_to_find_kth_smallest(k, limit, "unsorted", "randomized_quickselect")
    sorted_time_randomized_quickselect = time_to_find_kth_smallest(k, limit, "sorted", "randomized_quickselect")
    r_sorted_time_randomized_quickselect = time_to_find_kth_smallest(k, limit, "reverse_sorted", "randomized_quickselect")
    
    # print(unsorted_time_median_of_medians)
    # print(sorted_time_median_of_medians)
    # print(r_sorted_time_median_of_medians)
    # print(unsorted_time_randomized_quickselect)
    # print(sorted_time_randomized_quickselect)
    # print(r_sorted_time_randomized_quickselect)

    plt.figure(figsize=(12,8))
    plt.plot(arr_size, unsorted_time_median_of_medians, label='median_of_medians on unsorted array')
    plt.plot(arr_size, sorted_time_median_of_medians, label='median_of_medians on sorted array')
    plt.plot(arr_size, r_sorted_time_median_of_medians, label='median_of_medians on r_sorted array')

    plt.plot(arr_size, unsorted_time_randomized_quickselect, label='randomized_quickselect on unsorted array')
    plt.plot(arr_size, unsorted_time_randomized_quickselect, label='randomized_quickselect on r_sorted array')
    plt.plot(arr_size, unsorted_time_randomized_quickselect, label='randomized_quickselect on sorted array')

    plt.xlabel('Array Size')
    plt.ylabel('Time taken')
    plt.title('Time taken median_of_medians and randomized_quickselect')
    plt.legend()
    plt.savefig('select_time.png')