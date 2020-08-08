"""
Problem Description: Given an array of integers, A of length N, find out the
maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the
second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the
sub-array.

Find and return the required subarray.

NOTE: If there is a tie, then compare with segment's length and return segment
which has maximum length. If there is still a tie, then return the segment with
minimum starting index.

Problem Constraints: 1 <= N <= 10^5 -10^9 <= A[i] <= 10^9

Example Input Input 1: A = [1, 2, 5, -7, 2, 3] Input 2: A = [10, -1, 2, 3, -4,
100]

Example Output Output 1: [1, 2, 5] Output 2: [100]

# Algorithm

Find the first non-negative integer and do a running sum until the next
non-negative integer. Put the running sum and start/end index of this subarray
in a tuple.

Loop through and do this until end of array. If new rs > oldrs, replace rs with
new rs and new start/end index. if rs is same, store the one with longest
length. If rs is same and length is same, continue.

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start_index = 0
        subarray_sum = 0
        subarray_start = None
        subarray_end = 0        
        result = {
            "sum": -1,
            "start_index": 0,
            "end_index": 0
        }

        while start_index < len(A):
            # positive number
            if A[start_index] >= 0:
                if subarray_start == None:                    
                    subarray_start = start_index

                subarray_sum += A[start_index]
                subarray_end = start_index
            # negative number
            else:
                subarray_start = None
                subarray_sum = 0

            # check if running sum and length of the subarray from current
            # iteration is greater than or equal to subarray from previous
            # iteration
            if (subarray_start != None):
                if (subarray_sum > result["sum"]):
                    result["sum"] = subarray_sum
                    result["start_index"] = subarray_start
                    result["end_index"] = subarray_end
                elif (subarray_sum == result["sum"]):
                    if (subarray_end - subarray_start) > (result["end_index"] - result["start_index"]):
                        result["start_index"], result["end_index"] = subarray_start, subarray_end

            start_index += 1
        
        if result["sum"] == -1:
            return []
        else:
            return A[result["start_index"] : result["end_index"]+1]


A = [-1, -1, -1, -1]
s = Solution()
print(s.maxset(A))