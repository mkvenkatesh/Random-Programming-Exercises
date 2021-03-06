"""
# Counting sort 
# Same as original counting sort but instead of initializing a count array from 
# 0 to max key element, do it from min to max key element of the input array.

It operates by counting the number of objects that have each distinct key value,
and using arithmetic on those counts to determine the positions of each key
value in the output sequence. Its running time is linear in the number of items
and the difference between the maximum and minimum key values, so it is only
suitable for direct use in situations where the variation in keys is not
significantly greater than the number of items.

# Complexity
Time Worst Case - O(n + k) where k is the max element in the array of size n
Space - O(n + k)

# Algorithm
count = array of k+1 zeros for x in input do count[key(x)] += 1 total = 0 for i
in 0, 1, ... k do count[i], total = total, count[i] + total output = array of
the same length as input for x in input do output[count[key(x)]] = x
count[key(x)] += 1 return output
"""

# [5, 4, 3, 2, 1, 1, 5]

def get_minmax_key(array):
    min_key = 0
    max_key = 0
    for i in array:
        if i < min_key:
            min_key = i
        if i > max_key:
            max_key = i
    return min_key, max_key

def counting_sort(array):
    sorted_array = []
    # initialize a count array with enough space to store the input array
    # histogram. Initialize from min to max key element of input array.
    min_key, max_key = get_minmax_key(array)
    count = [0] * ((max_key - min_key) + 1)

    # loop through input array to build the histogram
    for key in array:
        count[key-min_key] += 1

    # calculate the running sum on the count array, which indicates where each
    # key in input array, which is now mapped to the index of count array,
    # should appear in the output
    running_sum = 0
    for idx in range(0, len(count)):
        count[idx], running_sum = running_sum, running_sum + count[idx]

    # Build the sorted array by looping through the original array and finding
    # the correct index for the array key from count array
    sorted_array = [None] * len(array)
    for key in array:
        sorted_array[count[key-min_key]] = key
        count[key-min_key] += 1

    return sorted_array


input_array = [5, 4, 3, 2, 5, 8]
print(counting_sort(input_array))