# Big O is O(2^N)
# Fibonacci sequence - 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Rule is Xn = Xn-1 + Xn-2
def fib(n):
    # check that the input is an integer
    if (type (n) != int):
        raise TypeError("n must be a positive integer")
    elif (n < 0):
        raise ValueError("n must be a positive integer")
    else:
        if (n==0 or n==1):
            return 1
        else:
            return fib(n - 1) + fib (n - 2)

print(fib(5))

# fib(3)
# fib(2) + fib(1)
# fib(1) + fib(0) + fib(1) = 3


# fib(5)
# fib(4) + fib(3)
# fib(3) + fib(2) + fib(2) + fib(1)
# fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + 1
# fib(1) + fib(0) + 1 + 1 + 1 + 1 + 1 + 1
# 1 + 1 + 6
# 8