"""
12 = 1, 2, 3, 4, 6, 12
75 = 1, 3, 5, 15, 25, 75

- - - - - - - - - - - -
Options:
1. Loop through all numbers from 2 to n/2
2. Loop from 2 to sqrt(n)
    if % == 0, add to list of factors
    add // to the list as well (make sure to check it's not already in the list)

"""
import math 

def count_numbers_factors(n):
    n = abs(n)
    if n == 1:
        return 1
    elif n == 0:
        return 0

    count = 2
    for i in range(2, int(math.sqrt(n)) + 1): #
        if n % i == 0: # if n is divisible by i, add it to factor list
            count += 1
            # if n is divisible by i, and as long as n//i != i (i.e. it's
            # already in the factor list, then n//i is also a factor)
            if n//i != i: 
                count += 1
    return count


print(count_numbers_factors(-20))