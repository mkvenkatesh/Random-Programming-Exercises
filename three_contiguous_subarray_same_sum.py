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
Efficient Approach [ O(A) solution ] :
1. If sum of all the elements of the array is not divisible by 3, return 0.
2. It is obvious that the sum of each part of each contiguous part will be equal
   to the sum of all elements divided by 3.
3. Let’s create an array cnt[ ], where cnt[ i ] equals 1, if the sum of elements
   from ith to Ath equals Array_Sum/3 else 0. Now, calculate the cumulative sum
   of the cnt array from the last index.
4. Thus, we receive very simple solution: for each prefix of initial array 1…i
   with the sum that equals Array_Sum/3 we need to add to the answer sums[i+2]

"""

class Solution:
    def solve(self, A, B):
        total = sum(B)

        # The array sum has to be divisible of 3, otherwise no solution is
        # possible
        if total % 3 == 0:
            target = total // 3 # 0, 1, 2, 3...
        else:
            return 0

        answer = 0
        first_part = 0
        running_sum = 0
        
        for i in range(A - 1):
            running_sum += B[i]

            # 2nd 1/3rd of the array
            if running_sum == 2 * target:
                answer += first_part

            # 1st 1/3rd of the array
            if running_sum == target:
                first_part += 1
        
        return answer

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
