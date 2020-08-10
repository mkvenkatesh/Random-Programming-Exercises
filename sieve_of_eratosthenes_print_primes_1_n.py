""" The Sieve of Eratosthenes will generate all the primes from 2 to a given
number n. It begins by assuming that all numbers are prime. It then takes the
first prime number and removes all of its multiples. It then applies the same
method to the next prime number. This is continued until all numbers have been
processed. For example, consider finding primes in the range 2 to 20. We begin
by writing all the numbers down:


2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

2 is the first prime. We now cross out all of its multiples, ie every second
number:


2 3  5  7  9  11  13  15  17  19

The next non-crossed out number is 3 and thus it is the second prime. We now
cross out all the multiples of 3, ie every third number from 3:


2 3 4 5  7 8  10 11 13 14 16 17 19 20

All the remaining numbers are prime and we can safely terminate the algorithm.
"""
import math
import time

start_time = time.time()

def sieve_get_primes(n):
    # Initial array is assumed to be all primes
    prime_candidates = [True] * (n + 1) 
    # set the first two elements 0 and 1 to be not primes
    prime_candidates[0] = False
    prime_candidates[1] = False

    for num in range(2, int(math.sqrt(n)) + 1):
        if(prime_candidates[num]):        
            for prime_idx in range(num * num, n + 1, num):                
                prime_candidates[prime_idx] = False

    return prime_candidates

primes = sieve_get_primes(1200)
for idx, val in enumerate(primes):
    if (val):
        print(idx, end=' ')
print()

print(f"--- Total seconds: {time.time() - start_time} ---")