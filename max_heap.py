"""
Heap data structure - max heap

A heap is a complete binary tree that satisfy the heap property:
1. For max-heap, the root element needs to be bigger than its children
2. For min-heap, the root element needs to be smaller than its children

Complete binary tree is a binary tree with all its levels full except for the
last level and whatever is left at the leaves should lean towards the left of
the tree. 

This completeness property gives an interesting property in array representation
of the tree, where for a given index i, 2i+1 represents the left child of i,
2i+2 represents the right child of i and (i-1)/2 represent the i'th parent

Max or Min heap makes use of a recursive function called heapify to ensure that
a given indexed position in an array satisfies the heap property in the tree.

The root element gives the largest or the smallest value. If the root needes to
be deleted, you should swap the last element in the array (last leaf node) with
the root, remove last element and run heapify on root node. This is the same for
removing any element in the tree.

To insert an element, you insert at the end of the array and run heapify on all
non-leaf nodes

"""


def heapify(arr, n, i):
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    if (left < n) and (arr[left] > arr[largest]): # for min-heap, change this condition
        largest = left
    
    if (right < n) and (arr[right] > arr[largest]): # for min-heap, change this condition
        largest = right

    # if largest index is different from i, swap them and call heapfiy
    # recursively on the swapped element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        if largest <= (n//2) - 1: # no need to call heapify on leaf nodes
            heapify(arr, n, largest)

def insert(arr, elem):
    
    # insert the new element to the end of the array/tree
    arr.append(elem)

    arr_len = len(arr)
    # if there's no nodes in the tree, this would be the first element so return
    if arr_len == 1:
        return

    # ensure if we even need to heapify everything because of the new insertion.
    # Check the last element with its parent
    if elem <= arr[((arr_len-1)-1)//2]:
        return

    # if there are more than 1 element, then we need to heapify all non-leaf
    # nodes. (n//2)-1 index gives the last non-leaf node in the binary tree. Go
    # backwards to get the rest of the non-leaf nodes and apply heapify
    for i in range((arr_len//2)-1, -1, -1):
        heapify(arr, arr_len, i)


def remove(arr, elem):
    arr_len = len(arr)
    # find the index of the element
    try:
        remove_index = arr.index(elem)
    except:
        print(f"Element {elem} not found in the heap!")
        return

    # Swap the elem with last node in the array/tree, delete the last element
    # and call heapify on entire array (non-leaf) if the removed element wasn't
    # a leaf
    arr[remove_index], arr[arr_len-1] = arr[arr_len-1], arr[remove_index]
    arr.pop() # remove the last element
    for i in range((len(arr)//2) - 1, -1, -1):
        heapify(arr, len(arr), i)


work_array = []
insert(work_array, 3)
insert(work_array, 4)
insert(work_array, 9)
insert(work_array, 5)
insert(work_array, 2)
insert(work_array, 1)
insert(work_array, 3)
insert(work_array, 10)

print(f"max-heap array: {str(work_array)}")

remove(work_array, 4)
print(f"max-heap array: {str(work_array)}")
remove(work_array, 10)
print(f"max-heap array: {str(work_array)}")