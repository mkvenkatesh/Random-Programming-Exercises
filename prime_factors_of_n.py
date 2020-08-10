"""
Given an integer N, for which 2 <= N <= 10^12, find its prime factors. The
result must be a list of sorted prime numbers where each number is listed as
many times as it is present in the prime decomposition of N.

Here are a few examples to make this clear:

For N=20 the prime decomposition is 20 = 2 * 2 * 5, so you must return 2, 2, 5.

For N=64 the prime decomposition is 64 = 2 * 2 * 2 * 2 * 2 * 2, result must be
2, 2, 2, 2, 2, 2.

For N=1105 the prime decomposition is 1105 = 5 * 13 * 17, result must be 5, 13,
17.

For N=9901 the prime decomposition consists of the number 9901 itself, so the
result must be a list with one element 9901 (9901 is a prime number).

You must write a function, which accepts one parameter - the number N and
returns the list of sorted prime numbers in the prime decomposition of N.

# Algo
We don't have to check if the numbers are prime. Starting with 2 and going up,
we can be sure that if a number divides N then it is a prime divisor. Let's
assume this is not true and following our algorithm we reach a number M that
divides N but is not prime. This would mean that this number M has prime
divisors. But these prime divisors are also divisors of N and they will be
smaller than M. This means that we should have already processed them and should
have divided the number N by them. We reached a contradiction with our initial
assumption. 

We iterate over the numbers in increasing order and we divide N by
each found number P that divides it, until N is still divisible by P.

"""
import math

def all_prime_factors(n):
    prime_factors = []

    for num in range(2, int(math.sqrt(n)) + 1):        
        while (n % num == 0):
            prime_factors.append(num)
            n = n // num
        
        if n == 1:
            break


    if n != 1:
        prime_factors.append(n)

    return prime_factors

print(all_prime_factors(1105))