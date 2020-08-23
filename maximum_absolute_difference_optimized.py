"""

Max Absolute Difference - Optimized

You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of
f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|,
where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0 f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3 f(1,3)
= f(3, 1) = |1 - (-1)| + |1 - 3| = 4 f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| =
5

So, we return 5.

# Algorithm
Just try to expand this expression and see what all possible values can they be
without using ABSOLUTE OPERATORS |A[i] - A[j]| + |i - j|

It should boil down to following 4 values (because |x-y| = |y-x|).

(A[i]-A[j]) + (i-j) (-A[i]+A[j]) + (i-j)  
(A[i]-A[j]) + (-i+j) (-A[i]+A[j]) + (-i+j)

Let’s try to be symmetrical here by organizing above four expressions.

(A[i]-A[j]) + (i-j)   = (A[i]+i) - (A[j]+j) (-A[i]+A[j]) + (i-j)  = (A[j]-j) -
(A[i]-i) (A[i]-A[j]) + (-i+j)  = (A[i]-i) - (A[j]-j) (-A[i]+A[j]) + (-i+j) =
(A[j]+j) - (A[i]+i)

If we ignore indices i and j. Then 1, 4 is same and 2, 3 are same.

So it boils down to two final expressions: Difference of sums: (A[i]+i) -
(A[j]+j) or Difference of differences: (A[i]-i) - (A[j]-j)

We need to find which one yields max value of these.

max((|a[i]-a[j]) + (i-j)) for each i,j = max((a[i]+i)-(a[j]+j),
(a[i]-i)-(a[j]-j)) for each i,j = max( max(a[i]+i) - min(a[i]+i), max(a[i]-i) -
min(a[i]-i) )

Why max-min works?: When you maximise (A[i] + i) and minimise (A[j] + j) then
automatically their difference will be maximum. For e.g for the given array
[1,3,-1], ai+i (or aj+j) will be [1, 4, 1]. Maximum of (ai+i) - (aj+j) will be
max(1-4, 1-1, 4-1) = max(-3, 0, 3) = 3 (which is max(ai+i)-min(aj+j) i.e. 4-1)
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = A[0]
        min1 = A[0]
        max2 = A[0]
        min2 = A[0]

        for index in range(len(A)):
            if A[index] + index > max1:
                max1 = A[index] + index
            
            if A[index] + index < min1:
                min1 = A[index] + index
            
            if A[index] - index > max2:
                max2 = A[index] - index

            if A[index] - index < min2:
                min2 = A[index] - index

        return max(max1-min1, max2-min2)

A = [1, 3, -1]

s= Solution()
print(s.maxArr(A))        