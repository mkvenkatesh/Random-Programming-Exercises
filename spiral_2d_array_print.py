class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers

    # Problem: 
    # Given a matrix of m * n elements (m rows, n columns), 
    # return all elements of the matrix in spiral order.

    # Input: 
    #[
    #  [ 1, 2, 3 ],
    #  [ 4, 5, 6 ],
    #  [ 7, 8, 9 ]
    #]

    # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Algorithm:
    # 1. There are four directions you could go - Right, Down, Left and Up
    # 2. Once you go in this direction, you can delete the seen elements.
    # 2.1 In order to mark the seen elements, use four variables Top, Left, Right, Bottom
    #     to mark the index of the matrix that you have already seen. Increment/Decrement
    #     these appropriately based on the direction.
    def spiralOrder(self, A):
        top = 0
        right = len(A[top]) - 1
        left = 0
        bottom = len(A) - 1
        result = []
        dir = "right"
        
        while (left <= right and top <= bottom):
            if (dir == "right"):
                for i in range(left, right + 1):
                    result.append(A[top][i])
                top += 1
                dir = "down"
            
            elif (dir == "down"):
                for i in range(top, bottom + 1):
                    result.append(A[i][right])
                right -= 1
                dir = "left"

            elif (dir == "left"):
                for i in range(right, left - 1, -1):
                    result.append(A[bottom][i])
                bottom -= 1
                dir = "top"
                
            elif (dir == "top"):
                for i in range(bottom, top - 1, -1):
                    result.append(A[i][left])
                left += 1
                dir = "right"   
        
        return result

s = Solution()

input = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

print(s.spiralOrder(input))