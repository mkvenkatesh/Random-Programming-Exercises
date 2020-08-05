"""
Implement a program, which given an integer n, computes the sum of its digits.
If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum
is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.

# Algorithm
simple
Another algorithm is to convert this to a string/list and easily loop over
e.g: sum([int(x) for x in str(abs(n))])
"""
36028797018963968
def digit_sum(n): #O(N) where N is len(N)
    n = abs(n)

    if n < 10:
        return n
    else:
        num_sum = 0

        while n > 0:
            num_sum += (n % 10)
            n = n // 10 # // for integer division. Don't use floating point since it will have some rounding issues.
            
        return num_sum

print(digit_sum(2**55))