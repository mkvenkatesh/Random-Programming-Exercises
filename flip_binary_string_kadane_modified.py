"""

Flip

You are given a binary string(i.e. with characters 0 and 1) S consisting of
characters S1, S2, …, SN. In a single operation, you can choose two indices L
and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By
flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of
1s is maximised. If you don’t want to perform the operation, return an empty
array. Else, return an array consisting of two elements denoting L and R. If
there are multiple solutions, return the lexicographically smallest pair of L
and R.

Notes:
Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, 
if a == c and b < d.

For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string.
So, we return [1, 1].

Another example,

If S = 111

No operation can give us more than three 1s in final string. So, we return empty
array [].

# Algorithm

If the string is all 1's return []
if not, find the maximum subarray with count(0)-count(1)

# 011001001

0: 0
1: [0][01] - max(number of 0's-1's in [0], number of 0's-1'st in [01])
2: [01][011] - max(number of 0's-1's in [01], number of 0's-1'st in [011])
"""


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if A == "1" * len(A):
            return []

        current_count = 0
        max_count = None
        start_index = 0
        end_index = 0
        temp_index = 0

        for idx, val in enumerate(A):
            if val == "0":
                current_count += 1
            else:
                current_count -= 1

            if max_count == None:
                max_count = current_count

            if (current_count > max_count):
                max_count = current_count
                start_index = temp_index
                end_index = idx
            
            if (current_count < 0): # number of 1's has exceeded number of 0's
                current_count = 0
                temp_index = idx + 1

        return (start_index + 1, end_index + 1)

A = "011001001"
s = Solution()
print(s.flip(A))