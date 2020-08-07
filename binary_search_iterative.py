"""
Binary Search - Iterative Approach 

Given a sorted array, return the index of the element that needs to be searched.
Return -1 if no match is found

Worst case - O(log N)
Time complexity - O(1)

# Algorithm


while True:
    if start > end:
        break
    mid = start + end/2
    if key is in mid return
    elif key < mid
        end = mid -1
    elif key > mid
        start = mid + 1


# Example

[1, 3, 4, 5, 10, 14, 17, 21, 22, 22, 27, 40, 51]

"""

def binary_search(array, key):
    start = 0
    end = len(array) - 1
    while True:
        if start > end:
            return -1

        mid = (start + end) // 2
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            end = mid -1
        elif key > array[mid]:
            start = mid + 1

input_array = [1, 3, 4, 5, 10, 14, 17, 21, 22, 22, 27, 40, 51]
print(binary_search(input_array, 22))