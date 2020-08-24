"""
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to
determine the number of contiguous subarrays that fulfills the following
conditions:

    The value at index i must be the maximum element in the contiguous subarrays, and
    These contiguous subarrays must either start from or end on index i.

Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000

Output
An array where each index i contains an integer denoting the maximum number of
contiguous subarrays of arr[i]

Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]

Explanation:

    For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
    For index 1 - [4], [3, 4], [4, 1]
    For index 2 - [1]
    For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
    For index 4 - [2]

So, the answer for the above input is [1, 3, 1, 5, 1]
"""

a = [3, 4, 1, 6, 2]
#a = [1,2,3,4,5]

n = len(a)
lans = [0] * n
s = []

# Calculating the left subarray for a given index that satisfy the given
# conditions is the same as calculating it for reverse of the array. So if Li is
# the left subarray counts and Ri is the left subarray for the reversed array
# counts then the final answer ans = Li + Ri -1

# To calculate L1 efficient we can use the previously stored information on
# counts using a stack
for i in range(n):
    while len(s) > 0 and a[s[-1]] < a[i]:
        lans[i] += lans[s.pop()]
    s.append(i)
    lans[i] += 1

rans = [0] * n
s = []
for i in range(n-1, -1, -1):
    while len(s) > 0 and a[s[-1]] < a[i]:
        rans[i] += rans[s.pop()]
    s.append(i)
    rans[i] += 1

for i in range(n):
    lans[i] = lans[i] + rans[i] - 1

print(lans)