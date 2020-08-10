"""
Given an integer n, calculate the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and 1 + 2 + 4 + 8 = 15 The
divisors of 7 are 1 and 7, which makes the sum 8.

The input number n will be in the range [1, 10^9].

Return one number - the sum of divisors of n.

Input 	Output
8 	    15
7 	    8
1 	    1
1000 	2340

# Algo
1. Find all factors of n
    1.1 Find all factors from 2 to sqrt(n) n % i and n/i are factors of n
2. Sum all the factors
"""

import math

def sum_the_divisors(n):
    # Write your code here
    divisors = get_all_divisors(n)
    return sum(divisors)


def get_all_divisors(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    
    divisors = [1, n]
    
    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            divisors.append(num)
            if n//num != num:
                divisors.append(n//num)
    
    #print(divisors)
    return divisors

print(sum_the_divisors(20))