"""
Sort the Files Lexicographically

# Problem 
Your task is given N to return the sorted lexicographically list of file names.
N is in the range [1, 1,000,000]. In 40% of the test cases N will be no higher
than 1,000. If N if higher than 1,000 return just the first 1,000 file names.

SAMPLE INPUT 
16

SAMPLE OUTPUT 
IMG1.jpg IMG10.jpg IMG11.jpg IMG12.jpg IMG13.jpg IMG14.jpg
IMG15.jpg IMG16.jpg IMG2.jpg IMG3.jpg IMG4.jpg IMG5.jpg IMG6.jpg IMG7.jpg
IMG8.jpg IMG9.jpg

# Listen/Questions
# Example
# Algorithm - BruteForce/Bud/Space-Time
# Algo Walkthrough
# Code
# Walkthough
# Test cases

# Algo

1. Generate string range from 1 to N
2. Use quicksort
"""

import time
start_time = time.time()

def file_sort_lexi(n, result):
    if n == 1:
        return [1]
    for i in range(1, n + 1):
        result.append('IMG' + str(i) + '.jpg')
    quick_sort(result, 0, len(result) - 1)
    if len(result) > 1000:
        result = result[:1000]
    return result

def quick_sort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)

# [4, 3, 1]
def partition(array, start, end):
    pivot_element = array[end]
    pivot_index = start

    for i in range(start, end):
        if array[i] <= pivot_element:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1
    
    array[pivot_index], array[end] = array[end], array[pivot_index]
    return pivot_index

result = []
file_sort_lexi(100, result)

print(result)

print("--- %s seconds ---" % (time.time() - start_time))