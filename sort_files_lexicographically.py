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
2. Throw the generated strings into a list and call a sorting algorithm*
3. Python comparison operators already does lexicographic sort on strings, so we
   can just use that for string sorting. If we have to implement this ourself,
   we can just create a function that takes two strings and returns true/false
   based on each character comparison

* Since only the first 1000 sorted elements are required, choose a sorting
  algorithm that works by sorting the first 1000 quickly and not worry about the
  whole N

- selection: min sorting, builds the sorted list from the left. O(N^2) = (n-1) + (n-2)...1000
- insert:  Build sorted list from left to right, bu comparing adjacent elements and placing them in the right position. Still bad. O(n^2)
- quick: partitioning sort. Pick an element and move elements < pivot to left else to right. Divide and conquer
- bubble: at the end of each iteration, the biggest element is placed at the end of the list using swapping and you proceed from 0 to N-1 and so on. O(N^2)
- merge: divide and conquer - O(N log n) but O(n) for space

Pick merge sort

"""

import time
start_time = time.time()

def file_sort_lexi(n, result):
    if n == 1:
        return [1]
    for i in range(1, n + 1):
        result.append('IMG' + str(i) + '.jpg')
    merge_sort(result, 0, len(result) - 1)
    if len(result) > 1000:
        result = result[:1000]
    return result

def merge_sort(array, start, end):
    if (start == end):
        return
    else:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        aux = merge(array, start, mid, mid + 1, end)
        array[start : end+1] = aux

def merge(array, start1, end1, start2, end2):
    aux = []

    while True:
        if (str(array[start1]) > str(array[start2])):
            aux.append(array[start2])
            start2 += 1
        elif (str(array[start1]) <= str(array[start2])):
            aux.append(array[start1])
            start1 += 1

        if (start1 > end1):
            aux += array[start2 : end2+1]
            break
        elif (start2 > end2):
            aux += array[start1 : end1+1]
            break    
    
    return aux


result = []
file_sort_lexi(100, result)
print(result)

print("--- %s seconds ---" % (time.time() - start_time))