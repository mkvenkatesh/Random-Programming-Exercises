# map (function, iter1, [iter2..]) - iterates through a list (or multiple if
# your function takes multiple arguments) and for each item it calls the
# function 

# 1, 1, 2, 3, 5, 8, 13
#                       fib(4)
#           fib(3)              fib(2)
#    fib(2)       fib(1)
# fib (1) fib(0)  
def fib(n, memo = {}):
    if (n==0 or n==1):
        return 1
    else:
        if n in memo:
            return memo[n]
        else:            
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
            return memo[n]

a = list(map(fib, range(10)))
print(a)


# Implementation of zip () with map
a = [1,2,3]
b = [4,5,6,7]
c = list(zip(a,b))
print(c)
c = list(map(lambda x,y: (x,y), a, b))
print(c)

# filter - While map() passes each element in the iterable through a function
# and returns the result of all elements having passed through the function,
# filter(), first of all, requires the function to return boolean values (true
# or false) and then passes each element in the iterable through the function,
# "filtering" away those that are false. It has the following syntax:
# filter(func, iterable)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
fil = list(filter(lambda x: x > 75, scores))
print(fil)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda x: x==x[::-1], dromes))
print(palindromes)


# reduce - reduce applies a function of two arguments cumulatively to the
# elements of an iterable, optionally starting with an initial argument. It has
# the following syntax: reduce(func, iterable[, initial])
from functools import reduce
list1 = [1,2,3,4,5,6,7]
l = reduce(lambda x,y: x+y, list1, 10)
print(l)