# Listen
# Big enough example
# Brute force approach first if possible and then proceed with optimization
# Algorithm Optimization (BUD)
#   1. BUD - Bottlenecks, Unnecessary Work, Duplicated Work

# have two arrays sorted and distinct, how do you find the common elements between the two arrays
# Brute force - two for loops O(A*B)
# Optimization 1 - Throw second array into a hash table and the lookup would be O(1), so it's O(A+B) run time and O(B) space complexity
# Optimization 2 - Binary search O(A*logB) runtime and O(1) space complexity
# Optimization 3 - Walthrough A & B array with two pointers - this will be O(A+B) runtime and O(1) space

# O(A*B)
array1 = (1, 2, 5, 6, 14, 29, 31)
array2 = (3, 5, 7, 8, 14, 16, 21, 25, 31)
common = []
for i in array1:
    for j in array2:
        if (i == j):
            common.append(i)

# iterate
# arrays are sorted
# O(A*B)
array1 = (1, 2, 5, 6, 14, 29, 31)
array2 = (3, 5, 7, 8, 14, 16, 21, 25, 31)
common = []
for i in array1:
    for j in array2:
        if (j > i):
            break
        elif (i == j):
            common.append(i)

# iterate
# arrays are sorted
# O(A*LogB)
array1 = (1, 2, 5, 6, 14, 29, 31)
array2 = (3, 5, 7, 8, 14, 16, 21, 25, 31)
common = []

def binary_search(search_val, start, end):
    mid = int((start+end)/2)
    if (search_val == array2[mid]):
        return True
    elif (search_val > array2[mid] and start != mid):
        start = mid
        return binary_search(search_val, start, end)
    elif (search_val < array2[mid] and end != mid):
        end = mid
        return binary_search(search_val, start, end)

for i in array1:
    if (binary_search(i, 0, len(array2))):
        common.append(i)


# Walk through each array with pointers
array1 = (1, 2, 5, 6, 14, 29, 31)
array2 = (3, 5, 7, 8, 14, 16, 21, 25, 31)
common = []

# two pointers ptr1 and ptr2 pointing to the first element in each array
# if ptr1.val == ptr2.val add to common list and increment both points
# else if ptr1.val < ptr2.val, increment ptr1, check equality again
# else if ptr1.val > ptr2.val, increment ptr2, check equality again
# break when ptr1 == len(array1) || ptr2 = len(array2)

def ptr_walk(ptr1, ptr2):
    if (ptr1 == len(array1) or ptr2 == len(array2)):
        return
    if array1[ptr1] == array2[ptr2]:
        common.append(array1[ptr1])
        ptr1 = ptr1 + 1
        ptr2 = ptr2 + 1
        ptr_walk(ptr1, ptr2)
    elif (array1[ptr1] < array2[ptr2]):
        ptr1 = ptr1 + 1
        ptr_walk(ptr1, ptr2)
    else:
        ptr2 = ptr2 + 1
        ptr_walk(ptr1, ptr2)

ptr_walk(0,0)        


print(common)
