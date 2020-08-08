"""

Min Steps in infinite Grid

Problem Description You are in an infinite 2D grid where you can move in any of
the 8 directions

 (x,y) to (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1),
    (x-1,y+1), (x+1,y-1) 

You are given a sequence of points and the order in which you need to cover the
points.. Give the minimum number of steps in which you can achieve it. You start
from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question
by trying out a few cases in the “See Expected Output” section.



Input Format Given two integer arrays A and B, where A[i] is x coordinate and
B[i] is y coordinate of ith point respectively.


Output Format Return an Integer, i.e minimum number of steps.


Example Input Input 1: A = [0, 1, 1] B = [0, 1, 2]



Example Output Output 1: 2

# Example
(-1,-1)----(-1,0)----(-1,1)------(-1,2)------(-1,3)
(0,-1)-----(0,0)-----(0,1)-------(0,2)-------(0,3)
(1,-1)-----(1,0)-----(1,1)-------(1,2)-------(1,3)
(2,-1)-----(2,0)-----(2,1)-------(2,2)-------(2,3)
(3,-1)-----(3,0)-----(3,1)-------(3,2)-------(3,3)

# Algorithm

Note that because the order of covering the points is already defined, the
problem just reduces to figuring out the way to calculate the distance between 2
points (A, B) and (C, D).

Note that what only matters is X = abs(A-C) and Y = abs(B-D).

While X and Y are positive, you will move along the diagonal and X and Y would
both reduce by 1. When one of them becomes 0, you would move so that in each
step the remaining number reduces by 1.

In other words, the total number of steps would correspond to max(X, Y).

"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        if len(A) == 0:
            return -1
        elif len(A) == 1:
            return 0

        steps = 0

        for i in range(0, len(A) - 1):
            row_diff = abs(A[i] - A[i+1])
            col_diff = abs(B[i] - B[i+1])
            steps += max(row_diff, col_diff)

        return steps
        
A = [0, 1, 1]
B = [0, 1, 2]
s = Solution()
print(s.coverPoints(A, B))
                