"""
Binary Search - Recursive Approach 

Given a sorted array, return the index of the element that needs to be searched.
Return -1 if no match is found

Worst case - O(log N)

Time complexity - O(log N) -- The recursive solution has O(log n)O(log \space
n)O(log n) memory complexity as it will consume memory on the stack.

# Algorithm

1. Check if key = array[mid], if so return index
2. if key < array[mid], call binary search on the first half of the array
3. if key > array[mid], call binary search on the second half of the array
4. return -1 if key is not found

# Example

[1, 3, 4, 5, 10, 14, 17, 21, 22, 22, 27, 40, 51]

"""

def binary_search(array, key, start, end):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2        
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            return binary_search(array, key, start, mid - 1)
        elif key > array[mid]:
            return binary_search(array, key, mid + 1, end)

input_array = [1, 3, 4, 5, 10, 14, 17, 21, 22, 22, 27, 40, 51]
print(binary_search(input_array, 22, 0, len(input_array) - 1))