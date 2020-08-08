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



Input Format
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y
coordinate of ith point respectively.


Output Format
Return an Integer, i.e minimum number of steps.


Example Input
Input 1:
A = [0, 1, 1] B = [0, 1, 2]



Example Output
Output 1: 2

# Example
(-1,-1)----(-1,0)----(-1,1)------(-1,2)------(-1,3)
(0,-1)-----(0,0)-----(0,1)-------(0,2)-------(0,3)
(1,-1)-----(1,0)-----(1,1)-------(1,2)-------(1,3)
(2,-1)-----(2,0)-----(2,1)-------(2,2)-------(2,3)
(3,-1)-----(3,0)-----(3,1)-------(3,2)-------(3,3)

# Algorithm

Take the first point. See if the next point is on the same row or column
If true:
    move towards the next point and increment step counter
else:
    move diagonally towards the next point and increment step

Repeat the above steps until all points are covered and return step

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

        current_point_index = 0
        steps = 0

        while current_point_index < (len(A) - 1):
            current_point = [A[current_point_index], B[current_point_index]]
            next_point = [A[current_point_index+1], B[current_point_index+1]]
            steps += self.get_steps_between_points(current_point, next_point)
            current_point_index += 1

        return steps

    def get_steps_between_points(self, current_point, next_point):
        steps = 0        
        while current_point != next_point:
            if (current_point[0] == next_point[0]): # two points on same row                
                temp = abs(current_point[1] - next_point[1])
                if current_point[1] < next_point[1]: # move to right                    
                    current_point[1] += temp
                else: # move to left
                    current_point[1] -= temp
                steps += temp
            elif (current_point[1] == next_point[1]): # two points on same column
                temp = abs(current_point[0] - next_point[0])
                if current_point[0] < next_point[0]: # move to top
                    current_point[0] += temp
                else: # move to bottom
                    current_point[0] -= temp               
                steps += temp      
            else: # move diagonally
                if next_point[0] < current_point[0] and next_point[1] < current_point[1]: # move top left
                    current_point[0] -= 1
                    current_point[1] -= 1
                elif next_point[0] > current_point[0] and next_point[1] < current_point[1]: # move bottom left
                    current_point[0] += 1
                    current_point[1] -= 1                
                elif next_point[0] < current_point[0] and next_point[1] > current_point[1]: # move top right
                    current_point[0] -= 1
                    current_point[1] += 1       
                else: # move bottom right
                    current_point[0] += 1
                    current_point[1] += 1
                steps += 1

        return steps

A = [0, 1, 1]
B = [0, 1, 2]
s = Solution()
print(s.coverPoints(A, B))
                