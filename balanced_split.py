"""
Balanced Split
Given an array of integers (which may include repeated integers), determine if
there's a way to split the array into two subarrays A and B such that the sum of
the integers in both arrays is the same, and all of the integers in A are
strictly smaller than all of the integers in B. Note: Strictly smaller denotes
that every integer in A must be less than, and not equal to, every integer in B.

Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if such a split is possible, and false otherwise.
Example 1
arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].
Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't
satisfy the requirement that all integers in A are smaller than all integers in
B.
"""
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
  # Write your code here
  # sort the array
  # have two pointers, one at the end and one at the beginning
  # maintain running sum with starting (add recurring ones to running sum), 
  # if rs_start >= end, decr end and keep rs_end
  # if left >= right and rs_start == rs_end, return true
  
  arr.sort()
  left = 0
  right = len(arr) - 1
  running_sum_left = arr[left]
  running_sum_right = arr[right]
  seen_count = 2
  while seen_count < len(arr):
    # to satisfy strictly less subarray condition, add all the recurring numbers to the running sum
    while arr[left] == arr[left+1]:
      left += 1
      seen_count += 1
      running_sum_left += arr[left]

    if (seen_count >= len(arr)):
        break

    # to satisfy strictly less subarray condition, add all the recurring numbers to the running sum
    while arr[right] == arr[right-1]:
      right -= 1
      seen_count += 1
      running_sum_right += arr[right]

    if (seen_count >= len(arr)):
        break

    if running_sum_left >= running_sum_right:
      right -= 1
      seen_count += 1
      running_sum_right += arr[right]
    else:
      left += 1
      seen_count += 1
      running_sum_left += arr[left]
      
  if (running_sum_left == running_sum_right):
    return True
  else:
    return False










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  