"""
Prime Counting

A classic math task is to count the prime numbers less than or equal to some
integer number N. In this task you have to write a function, which does this for
a given N, where 1 <= N <= 10^6. We don't count 1 a prime.

Here are a few examples:

For N=10, the prime numbers, which are less than or equal to 10 are: 2, 3, 5, 7.
The function must return 4. For N=31, the prime numbers are: 2, 3, 5, 7, 11, 13,
17, 19, 23, 29, 31. The function must return 11.

"""

import math

def prime_counting(n):
    # sieve or eratosthenes algorithm
    
    # initially all numbers are assumed prime
    prime_candidates = [True] * (n+1)
    prime_candidates[0] = False
    prime_candidates[1] = False
    
    # loop from 2 to square root of n
    for prime in range(2, int(math.sqrt(n)) + 1):
        if(prime_candidates[prime]):
            # loop through multiples of i and set them to False since they can't be prime
            for mul in range(prime * prime, n + 1, prime):
                prime_candidates[mul] = False
    
    prime_count = 0
    for val in prime_candidates:
        if(val):
            prime_count += 1
            
    return prime_count
                