""" 
You are given a list of non-negative integers and you start at the left-most
integer in this list. After that you need to perform the following step:

Given that the number at the position where you are now is P you need to
jump P positions to the right in the list. For example, if you are at
position 6 and the number at position 6 has the value 3, you need to jump to
position 6 + 3 = 9. Repeat this operation until you reach beyond the
right-side border of the list.

Your program must return the number of jumps that it needs to perform following
this logic. Note that the list may contain the number 0, which mean that you can
get stuck at a this position forever. In such cases you must return the number
-1.

The length N of the input list will be in the range [1, 1000]. 

SAMPLE INPUT
3 4 1 2 5 6 9 0 1 2 3 1

SAMPLE OUTPUT
4

# 0: 0 + 3 = 3, i = 1
# 3: 3 + 2 = 5, i = 2
# 5: 5 + 6 = 11, i =3
# 1: 1 + 11 = 12, i =4
# break

# Questions
1. If the previous jump ends at the last element in the list, do you return or count one more loop?

# Algorithm
just walk through the list
"""

def count_number_jumps(input_list): # Time is O(N) and space is O(1)
    if len(input_list) > 1000 or len(input_list) < 1:
        raise ValueError("Input list length should be 1 <= N <= 1000")

    count_jumps = 0
    index = 0
    while index < len(input_list):
        num = input_list[index]
        if num == 0:
            return -1
        else:
            count_jumps += 1
            index = num + index
    
    return count_jumps

print(count_number_jumps([3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1]))