"""
Worst case - O(N^2) Average Case - O(N Log N) Space - O(1)

# Algorithm

* At each step we choose a pivot element from the array. In most cases choosing
  right element is a good implementation choice.
* We then bring all the elements smaller than pivot to the left of pivot and all
  elements greater than pivot to the right side. The pivot is now at the correct
  position
* Now we can recurse for the left and right sub arrays and do the same
  partitioning as above

/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

# Example

[5, 4, 3, 2, 1, 29]

"""

def QuickSort(array, start, end):
    if start < end:
        # Get the index of the pivot element after it's placed in the right order in the array
        pivot_index = Partition(array, start, end)
        # Now do a recursive call to QuickSort for the left sublist
        QuickSort(array, start, pivot_index - 1)
        # Do a recursive call to QuickSort for the right sublist
        QuickSort(array, pivot_index + 1, end)

    return array

# [5, 4, 3, 2, 1, 29]
# [5, 4, 3, 2, 1, 2]
def Partition(array, start, end):
    pivot_element = array[end]
    pivot_index = 0

    # try to move elements in the array that's less than pivot element to the
    # left, and greater than pivot to the right
    for i in range(0, end):
        if array[i] <= pivot_element:            
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1
    # swap the pivot element to pivot index to fit it in the right place in the
    # array
    array[pivot_index], array[end] = array[end], array[pivot_index]
    return pivot_index


input_array = [5, 4, 4, 3, 2, 1, 29, 87, 66]
print(QuickSort(input_array, 0, len(input_array) - 1))