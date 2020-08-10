"""
Find the contiguous subarray within an array, A of length N which has the
largest sum. - use Kadane's algorithm

Input Format:

The first and the only argument contains an integer array, A.

Output Format:

Return an integer representing the maximum possible sum of the contiguous
subarray.

Constraints:

1 <= N <= 1e6 -1000 <= A[i] <= 1000

For example:

Input 1: A = [1, 2, 3, 4, -10]

Output 1: 10

Explanation 1: The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2: A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2: 6

Explanation 2: The subarray [4,-1,2,1] has the maximum possible sum of 6.

"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        
        # make sure you handle the base cases
        if (len(A) == 1):
            return A[0]
            
        current_max = A[0]
        total_max = A[0]

        for i in range(1, len(A)):
            current_max = max(current_max, 0) + A[i]
            total_max = max(current_max, total_max)        
                
        return total_max

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr = [-10, -1, -30]
s = Solution()
print(s.maxSubArray(arr))