"""
Find the contiguous subarray within an array, A of length N which has the
largest sum and return the index as well - use Kadane's algorithm


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

        current_sum = 0
        max_sum = None
        start_idx = 0
        end_idx = 0
        temp_idx = 0

        for idx, val in enumerate(A):
        
            if current_sum < 0:
                current_sum = val
                temp_idx = idx
            else:
                current_sum += val

            if max_sum == None:
                max_sum = current_sum
            else:
                if (max_sum < current_sum):
                    max_sum = current_sum
                    start_idx =  temp_idx
                    end_idx = idx
    
        return max_sum, start_idx, end_idx

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#arr = [-10, -1, -30]
s = Solution()
print(s.maxSubArray(arr))