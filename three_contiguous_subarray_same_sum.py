"""
Problem Description

You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3
contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])

sum1+sum2+sum3/3=0

Problem Constraints 1 <= A <= 105 -109 <= B[i] <= 109

Input Format First argument is an integer A. Second argument is an 1D integer
array B of size A.

Output Format Return a single integer denoting the number of ways to split the
array B into three parts with the same sum.

Example Input Input 1: A = 5 B = [1, 2, 3, 0, 3]

Input 2: A = 4 B = [0, 1, -1, 0]

Example Output Output 1: 2

Output 2: 1


# Algorithm
The key is to understand that for any solutions to exist the sum of the input
array should be divisible by 3. 

1. If the sum is not divisible by 3, return 0 
2. If not Loop through the first part of the array (which could by 0 to
   len(array)-2 i.e 1st part can take the whole array except the last two
   elements) 2.1 As you loop, add the indexes of the array into a new array
   (`first`) if the running sum equals to sum(array)/3. What this means is that
   the `first` array will hold all the possible indexes that could be part of
   the first 1/3rd of the subarray.

3. Loop through `first` array and for each index i in the `first array`, get the
   2nd 1/3rd of the array by going from array[i+1:]

3.1 for each item in array[i+1:], do a running sum and if running sum equals
sum(array)/3 then we increment our total count. What this means is that for a
given i value from `first` array, we are able to find the next part of the
array. 

Note: The last 1/3rd of the array can be completely ignored at this point.
Figuring out the combinations between part 1 and part2 of the array will get you
the answer you need.


"""

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        sums = sum(B)
        if sums % 3 != 0:
            return 0
        req_sum = sums//3
        var = 0
        first = set()
        total = 0
        ##indexes possible for first_sum end index 
        for i in range(A):
            var += B[i]
            if var == req_sum and i < A-2:
                first.add(i)

        for i in first:
            arr = B[i+1:]
            x = 0
            for j,value in enumerate(arr):
                x += value
                if x == req_sum and j < A-i-2:
                    total += 1
        return total

# B = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# B = [0, 1, -1, 0]
# B = [1, 2, 3, 0, 0, 3, 0]
B = [0, 0, 0, 0]
s = Solution()
print(s.solve(len(B), B))

# [0,0 ,0 ,0]
# [0] [0] [0,0]
# [0] [0,0] [0]
# [0,0] [0] [0]
