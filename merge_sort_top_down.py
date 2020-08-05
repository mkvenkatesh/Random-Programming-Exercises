"""
Merge Sort - Top Down

Worst/Best Case - O(N LogN)
Space - O(N)

# Algorithm
MergeSort(arr, i, j)
	if (i == j):
		return
	else:
		mid = (i + j) // 2
		MergeSort(arr, i, mid)
		MergeSort(arr, mid+1, j)
		MERGE(arr, i, mid, mid+1, j)
return arr

[4, 5, 6]
[1, 2, 3]

1,4, 5

"""

def MergeSort(array, start, end):
    if start == end:
        return
    else:
        mid = (start + end) // 2
        MergeSort(array, start, mid) # break and send the first half of the unsorted input sublist
        MergeSort(array, mid + 1, end) # break and send the second half of the unsorted input sublist
        Merge(array, start, mid, mid + 1, end) # Merge two sorted sublists
        return array

def Merge(array, arr1_start, arr1_end, arr2_start, arr2_end):
    auxiliary = []
    original_start = arr1_start
    original_end = arr2_end
    while True:
        # check for greater/lesser comparison and move the correct element to the aux list
        if (array[arr1_start] > array[arr2_start]):
            auxiliary.append(array[arr2_start])
            arr2_start += 1
        elif (array[arr1_start] <= array[arr2_start]):
            auxiliary.append(array[arr1_start])
            arr1_start += 1

        if (arr1_start > arr1_end or arr2_start > arr2_end):
            # add left over elements to the aux list
            if arr2_start > arr2_end:
                auxiliary += array[arr1_start:arr1_end+1]
            else:
                auxiliary += array[arr2_start:arr2_end+1]
            
            # copy the results back from aux to input list
            array[original_start:original_end + 1] = auxiliary
            break


input_array = [5, 4, 4, 3, 2, 1]
print(MergeSort(input_array, 0, len(input_array) - 1))