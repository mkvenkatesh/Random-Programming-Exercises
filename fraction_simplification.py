"""
Fraction Simplification

An operation very often performed on fractions is simplification to lowest
terms. If a fraction has numerator N and denominator D, then it is simple if N
and D don’t have any common divisors other than 1. Otherwise, the fraction can
be simplified to “lower terms” meaning that there is another fraction with the
same value where the numerator and denominator are smaller numbers than N and D.

Here are a few examples:

The fraction 3/7 cannot be simplified because 3 and 7 don’t have any common
divisors other than 1. The fraction 8/24 on the other hand, can be simplified to
1/3.

Write a function, which given two integers - the numerator and denominator of a
fraction returns the simplified fraction, possibly the same one as in the input.
To return the result the function will receive a third parameter - a list of two
elements in which you need to store the resulting numerator and denominator in
this order. In all programming languages the list supplied will have two
elements allocated that you need to fill with values.

The integers N and D will be in the range [1, 1,000,000,000].

Here is a sample test case:

SAMPLE INPUT

77 22

SAMPLE OUTPUT

7 2

"""
def simplify_fraction(numerator, denominator, result):
    # 8/24 = 1/3
    # 77/22 = 7/2 
    # find gcd of numerator and denominator and divide the num/den by gcd

    def gcd(A, B):
        if B > A:
            A, B = B, A
        if (B == 0):
            return A # return the remainder which is the GCD of (A,B)

        else:
            return gcd(B, A % B)
    
    div = gcd(numerator, denominator)
    result[0] = numerator // div
    result[1] = denominator //div

result = [0] * 2
simplify_fraction(77, 22, result)
print(result)