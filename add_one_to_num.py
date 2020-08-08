"""
# problem
Add 1 to number - don't use str/int/list functions

# Description
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:
If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]
as 123 + 1 = 124.

# Algorithm
carry = 0
result = digit[end] + 1
digit[end] = result % 10
carry = result //10
while carry:
    i--
    result = digit[i] + carry
    digit[i] = result % 10
    carry = result//10

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0
        index = len(A) - 1
        while True:
            if index == len(A) - 1:
                result = A[index] + 1
            else:
                result = A[index] + carry
            A[index] = result % 10
            carry = result // 10
            index -= 1

            if carry == 0:
                break

            if index < 0:
                A = [carry] + A
                break

        while A[0] == 0:
            del A[0]

        return A

s = Solution()
print(s.plusOne([0, 0, 9, 9, 9]))