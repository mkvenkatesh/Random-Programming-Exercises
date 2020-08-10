""" 
The greatest common divisor (GCD) of two numbers a and b is the greatest
number that divides evenly into both a and b. 
"""

# un-optimized
def gcd(a, b):
    for div in range(min(a, b), 0, -1):
        if (a % div == 0 and b % div == 0):
            return div

print(gcd(10,20))


# optimized - used euclid algorithm

"""
The Euclidean Algorithm for finding GCD(A,B) is as follows:

    If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
    If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
    Write A in quotient remainder form (A = B⋅Q + R)
    Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)

Find the GCD of 270 and 192

    A=270, B=192
    A ≠0
    B ≠0
    Use long division to find that 270/192 = 1 with a remainder of 78. We can write this as: 270 = 192 * 1 +78
    Find GCD(192,78), since GCD(270,192)=GCD(192,78)
"""

def gcd_euclid(A, B):
    if (B > A):
        A, B = B, A
    
    if (B == 0):
        return A # GCD for the initial input.
    else:
        return gcd_euclid(B, A % B)

print(gcd_euclid(8,25))

def lcm(A,B):
    return (A*B)//gcd_euclid(A, B)

print(lcm(20, 10))