"""
Merge Sort - Bottom Up

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

# Merge items of size 1
# merge items of size 2 next
# merge items of size 4 next
# merge items of size 8 next etc
"""

# [3, 2, 1, 0, 9, 8]
# [3] [2] [1] [0] [9] [8]
#   size 1 merge [3][2] [1][0] [9,8]
#   [2, 3] [0, 1] [8, 9]
# [2, 3] [0, 1] [8, 9]
#   size 2 merge [2, 3][0, 1] [8, 9]
#   [0,1, 2, 3] [8, 9]
# [0, 1, 2, 3] [8, 9]
#   size 4 merge [0, 1, 2, 3] [8, 9]
#   [0, 1, 2, 3, 8, 9]
# done
def MergeSort(array):
    size = 1

    while size <= len(array):
        start = 0
        end = 1
        while start < len(array) and end < len(array) :
            end = start + (size * 2) - 1
            
            if end >= len(array): 
                end = len(array) - 1
                if (end - start) < size:
                    break
            
            mid = start + size - 1

            MergeSubLists(array, start, mid, mid + 1, end)
            start += (size * 2) 

        size *= 2

    return array

def MergeSubLists(array, start1, end1, start2, end2):
    aux = []
    orig_start = start1
    orig_end = end2

    while True:
        if (array[start1] > array[start2]):
            aux.append(array[start2])
            start2 += 1
        elif (array[start1] <= array[start2]):
            aux.append(array[start1])
            start1 += 1
        
        if (start1 > end1) or (start2 > end2):
            # Copy rest of the elements left over if you finished one of the sublist
            if (start1 > end1):
                aux += array[start2:end2 + 1]
            else:
                aux += array[start1:end1 + 1]

            break
    
    # dump aux into original array
    array[orig_start:orig_end +1] = aux

input_array = [3, 2, 2, 9, 8, 90, 1, 2, 67, 23]
print(MergeSort(input_array))


