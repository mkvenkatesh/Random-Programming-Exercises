"""
# for n>=2 check if a number is prime or not
"""

import time

def is_prime(n):
    if (n < 2):
        raise ValueError("n has to be greater than or equal to 2")

    for i in range(2, n): # O(N)
        if n % i == 0:
            return False
    return True

start_time = time.time()
print(is_prime(6700417))
print(f"Elapsed time in seconds: {time.time() - start_time}")


def is_prime_optimized(n):
    if (n < 2):
        raise ValueError("n has to be greater than or equal to 2")

    for i in range(2, int(n ** (1/2))): # O(N^1/2))
        if n % i == 0:
            return False
    return True

start_time = time.time()
print(is_prime_optimized(6700417))
print(f"Elapsed time in seconds: {time.time() - start_time}")