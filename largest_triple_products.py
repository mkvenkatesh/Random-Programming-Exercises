"""
You're given a list of n integers arr[0..(n-1)]. You must compute a list
output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive),
output[i] is equal to the product of the three largest elements out of arr[0..i]
(or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).

Note that the three largest elements used to form any product may have the same
values as one another, but they must be at different indices in arr.

Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000].

Output
Return a list of n integers output[0..(n-1)], as described above.

Example 1
n = 5
arr = [1, 2, 3, 4, 5]

output = [-1, -1, 6, 24, 60]
The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.
"""

import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def findMaxProduct(arr):
    if len(arr) <= 2:
        return [-1, -1]
  
    output = [0] * len(arr)
    prev_prod_factors = []
    
    for i in range(len(arr)):

        if (i < 2):
            output[i] = -1
            prev_prod_factors.append(arr[i])
            continue

        if len(prev_prod_factors) < 3:
            prev_prod_factors.append(arr[i])
        else:
            prev_prod_factors.sort()
            if arr[i] > prev_prod_factors[0]:
                prev_prod_factors[0] = arr[i]

        output[i] = prev_prod_factors[0] * prev_prod_factors[1] * prev_prod_factors[2]
  
    return output

arr_1 = [2, 4, 7, 1, 5, 3]
print(findMaxProduct(arr_1))