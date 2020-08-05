# Listen
# Big enough example
# Brute force approach first if possible and then proceed with optimization
# Algorithm Optimization (BUD)
#   1. BUD - Bottlenecks, Unnecessary Work, Duplicated Work
#   2. Look for space-time tradeoffs
#   3. Do it yourself
#   4. Recursion

# Find permutations of s within b, s is a smaller string and b is a bigger string

# example
# s = "abbc"
# b =  "babcabbacaabcbabcacbb"

# STEP 1 - Find all permutations of the string s
#                              abc
#         0: [a][b,c]                   1:[b] [a,c]                 2:...       
#   0:[a,b][c]    1:[a,c][b]    0:[b,a][c]      1:[b,c][a]      ...     ...
#   0:[a,b,c][]   0:[a,c,b][]   0:[b,a,c][]      0:[b,c,a][]       ...     ...

# Brute force - O(N!)
def permute(choices, answers=[], final_list=[]):
    if choices == []:
        # print(''.join(answers))
        final_list.append(''.join(answers))
        return
    else:
        for i in range(len(choices)):
            new_choices = choices[:]
            new_choices.remove(new_choices[i])
            answers.append(choices[i])
            permute(new_choices, answers, final_list)
            answers.pop()

    return final_list

s = "abbc"
perm_list = permute(list(s))
print(perm_list)

# Another way of doing this
# def permute(a, l, r): 
#     if l==r: 
#         print(''.join(a))
#     else: 
#         for i in range(l,r+1): 
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 
  
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1) 


# STEP 2 - find all occurrences of permuntation of s in b
# s: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# b: babcabbacaabcbabcacbb

# put all the items in s in a hash table

# while True:
#  counter = 0
#  take the len(s) letters from b and check if a key exist, if so, print
#  if (counter+len(s)) <= len(b)
#       break
#  increment counter by 1

# O(B) , so total is O(N!) + O (B)
b =  "babcabbacaabcbabcacbb"
incr = 0
while True:
    key = b[incr:len(s)+incr]
    if key in perm_list:
        print(key)
    if incr + len(s) > len(b):
        break
    incr = incr + 1



# Optimized - BUD (Bottleneck, unnecessary, duplicate); space-time; dyi
# 
# s = "abbc"
# b =  "babcabbacaabcbabcacbb"

# if we take 4 letters at a time from b, does it have the same frequency as s?
# O(B)
for i in range(len(b)-len(s)+1):
    chunk = list(b[i:i+len(s)])
    for j in range(len(s)):
        if s[j] in chunk:
            chunk.remove(s[j])
    if chunk == []:
        print(b[i:i+len(s)])
        

    