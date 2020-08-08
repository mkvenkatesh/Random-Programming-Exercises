
"""
Problem Description Given a number A. 

Find the factorial of the number. Assume Python doesn't support BigInt and the
maximum int storage for 64 bit computer is 2^64. So large factorial inputs will
fail with this upperbound if we keep the result in an int.


Problem Constraints 1 <= A <= 100

Input Format First and only argument is the integer A.


Output Format Return a string, the factorial of A.

4 = 4 * 3 * 2 * 1 N = n * (n-1)!
"""

# This function finds factorial of large 
# numbers and prints them 
def factorial(n) : 
    res = [None]*1500
    # Initialize result 
    res[0] = 1
    res_size = 1
  
    # Apply simple factorial formula  
    # n! = 1 * 2 * 3 * 4...*n 
    x = 2
    while x <= n : 
        res_size = multiply(x, res, res_size) 
        x = x + 1
    i = res_size-1
    ans=""
    while i >= 0 : 
        ans+=chr(48+res[i]) 
        i = i - 1
    return ans

def multiply(x, res,res_size) : 
      
    carry = 0 # Initialize carry 
  
    # One by one multiply n with individual 
    # digits of res[] 
    i = 0
    while i < res_size : 
        prod = res[i] *x + carry 
        res[i] = prod % 10; # Store last digit of  
                            # 'prod' in res[] 
        # make sure floor division is used 
        carry = prod//10; # Put rest in carry 
        i = i + 1
  
    # Put carry in res and increase result size 
    while (carry) : 
        res[res_size] = carry % 10
        # make sure floor division is used 
        # to avoid floating value 
        carry = carry // 10
        res_size = res_size + 1
          
    return res_size

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        return factorial(A)


s = Solution()
print(s.solve(300))