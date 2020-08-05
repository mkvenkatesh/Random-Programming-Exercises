# Big O is O(K) where K is the height of the tre
# Fibonacci sequence - 0, 1, 1, 2, 3, 5, 8, 13, 21... 
# Rule is Xn = Xn-1 + Xn-2 

# With regular fibonacci code, you are duplicating a lot of function calls. For
# e.g, in the fib(5) call below, fib(3), fib(2) are called multiple times. We
# can avoid this by storing the value of each of the different fib calls. 

# In essence we cache the function calls, this is called memoization.

def fib(n, memo={}):
    # check that the input is an integer
    if (type(n) != int):
        raise TypeError("n must be a positive integer")
    elif (n < 0):
        raise ValueError("n must be a positive integer")
    else:
        if (n==0 or n==1):
            return 1
        elif (n in memo):
            return memo[n]
        else:
            memo[n] = fib(n - 1) + fib (n - 2)
            return memo[n]

print(fib(5))

# fib(3)
# memo[3] = fib(2) + fib(1)

# memo[3] = (memo[2] = fib(1) + fib(0)) + 1
# memo[3] = (memo[2] = 2) + 1
# memo[3] = 3
