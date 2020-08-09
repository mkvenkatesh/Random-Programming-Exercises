"""

Max Absolute Difference

You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of
f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|,
where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0 
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3 
f(1,3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4 
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        # get max and min value and index of A
        max_a = A[0]
        min_a = A[0]
        max_idx = 0
        min_idx = 0
        max_candidate = []
        min_candidate = []        
        for index,val in enumerate(A):
            if val > max_a:
                max_a = val
                max_idx = index
            if val < min_a:
                min_a = val
                min_idx = index

        # add them to potential candidates for getting the max absolute difference
        max_candidate.append((max_a, max_idx))
        min_candidate.append((min_a, min_idx))

        for index,val in enumerate(A):
            if val >= max_a - len(A) - max_idx:
                max_candidate.append((val, index))
            if val <= min_a + len(A) + min_idx:
                min_candidate.append((val, index))
        
        max_abs = 0
        for i in max_candidate:
            for j in min_candidate:
                abs_val = abs(i[0] - j[0]) + abs(i[1] - j[1])
                if abs_val > max_abs:
                    max_abs = abs_val

        return max_abs



A = [ 86, 19, 46, 56, 14, 67, 19, 53, 15, 59 ]

s= Solution()
print(s.maxArr(A))