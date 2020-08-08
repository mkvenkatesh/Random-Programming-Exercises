"""
Problem Description
Given a number A. Find the fatorial of the number.


Problem Constraints
1 <= A <= 100


Input Format
First and only argument is the integer A.


Output Format
Return a string, the factorial of A.

4 = 4 * 3 * 2 * 1
N = n * (n-1)!
"""

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        if A == 0 or A == 1:
            return A
        else:
            return A * self.solve(A - 1)

s = Solution()
print(s.solve(300))