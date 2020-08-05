"""
Implement a function, which given an integer computes if it's a palindrome.

Input
One integer n, where 0 < n <= 10,000,000,000.

Output
Your function must return a boolean true if n is a palindrome and false otherwise.

# Example
1: true
11: true
101: true
12222221: true
1232423542132: false
991283123: false

Algorithm

1. Convert the number to string, reverse it and see if it matches the original string
2. modulo/divide by looping over the number and get the reverse of the number and see if it matches
3. get the first and last digits by dividing the number N by 10^(L-1) where L is the length of the number and get the last digit by N % 10 and compare
"""

def is_num_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

print(is_num_palindrome(110))