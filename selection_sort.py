"""
Worst case - O(N^2); Space - O(1)

# Algorithm

The idea behind this algorithm is pretty simple. We divide the array into two parts: sorted and unsorted. The left part is sorted subarray and the right part is unsorted subarray. Initially, sorted subarray is empty and unsorted array is the complete given array.
We perform the steps given below until the unsorted subarray becomes empty:
	1. Pick the minimum element from the unsorted subarray.
	2. Swap it with the leftmost element of the unsorted subarray.
	3. Now the leftmost element of unsorted subarray becomes a part (rightmost) of sorted subarray and will not be a part of unsorted subarray.

FindMinIndex(Arr[], start, end)    
        min_index = start    
        
        FOR i from (start + 1) to end:    
            IF Arr[i] < Arr[min_index]:    
                min_index = i    
            END of IF    
        END of FOR    
              
  Return min_index

SelectionSort(Arr[], arr_size):    
        FOR i from 1 to arr_size:    
            min_index = FindMinIndex(Arr, i, arr_size)    
        
            IF i != min_index:    
                swap(Arr[i], Arr[min_index])    
            END of IF    
        END of FOR


# Example

[5, 4, 3, 2, 1, 29]

"""

def selection_sort(array):
    sorted_index_end = 0
    unsorted_index_start = 1
    unsorted_index_end = len(array) - 1

    for index in range(unsorted_index_start, unsorted_index_end + 1):
        min_index = get_min_index(array, index)
        if array[sorted_index_end] > array[min_index]:
            array[sorted_index_end], array[min_index] = array[min_index], array[sorted_index_end]

        sorted_index_end += 1

    return array

def get_min_index(array, index):    
    min_index = index
    for i in range(index + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index

input_array = [5, 4, 4, 3, 2, 1, 29, 87, 66]
print(selection_sort(input_array))