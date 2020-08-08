"""
Find the contiguous subarray within an array, A of length N which has the
largest sum.

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
            
        running_sum = 0
        max_sum = None

        for i in range(0, len(A)):
            running_sum += A[i]
            # if input is all negative, make sure to get the maximum negative
            # integer. Setting max_sum to None initially will help get that max
            # negative value properly
            if max_sum == None: 
                max_sum = running_sum
            else:
                max_sum = max(running_sum, max_sum)
            
            # if running sum drops below 0, reset the running sum to 0 to reset
            # the array boundary for calculating the next max value
            if running_sum < 0:
                running_sum = 0
                
        return max_sum