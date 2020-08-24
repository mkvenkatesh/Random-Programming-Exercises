"""
Pair Sums

Given a list of n integers arr[0..(n-1)], determine the number of different
pairs of elements within it which sum to k. If an integer appears in the list
multiple times, each copy is considered to be different; that is, two pairs are
considered different if one pair includes at least one array index which the
other doesn't, even if they include the same values.

Input n is in the range [1, 100,000]. Each value arr[i] is in the range [1,
1,000,000,000]. k is in the range [1, 1,000,000,000].

Output Return the number of different pairs of elements which sum to k.

Example 1 n = 5 k = 6 arr = [1, 2, 3, 4, 3] output = 2 The valid pairs are 2+4
and 3+3.

Example 2 n = 5 k = 6 arr = [1, 5, 3, 3, 3] output = 4 There's one valid pair
1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th
elements, and 4th and 5th elements).

Solution 1: We can first sort the array and then iterate inwards from the
outside edges by maintaining two pointers. Consider adding the two numbers at
indices 0 and n-1. If this sum is less than k, we increment the left pointer. If
this sum is greater than k, we decrement the right pointer. If the sum is equal
to k, then we increment a count of valid pairs and move both pointers inwards.
We can repeat this process until the pointers meet. As stated, this solution
only works when all the values in the array are unique. To handle values that
appear multiple times, we can consider each block of the same value as a single
index in the array, but with a “weight” equal to the number of occurrences of
that value. For example, if the sorted array is [1, 2, 2, 2, 3, 4, 4] and k = 6,
then when our pointers are pointing at 2 and 4, we would increment our counter
of valid pairs not by 1, but by 3 * 2, the weights of 2 and 4 respectively. You
must take care in one particular case: when the pointers are both pointing at a
value which is exactly k/2. It’s incorrect to multiply the weight of this block
by itself, since that would count pairing up some indices with themselves. If
k/2 appears w times, then you must add w * (w - 1) / 2 valid pairs.

Solution 2: 

Let us iterate over the array once to build a hash table that maps each number
in the array to the number of times it occurs. For example, if our array is [2,
1, 3, 4, 2, 4, 2], then our hash table would look like:

{
  1: 1, 2: 3, 3: 1, 4: 2,
}

Now that we have these counts, we can iterate over the array one more time.
Every time we hit a value v, we can look up the number of times that k-v appears
in the array since that’s the exact number that we would need to form a pair
that sums to k. This method will count every pair twice, therefore we must take
care to divide by 2 at the end. In addition to that, ensure that you correctly
handle the same special case described in the previous solution, when v = k/2. q
"""


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
 	# Write your code here
  total_pairs = 0
  pair_ht = {}

  # build a histogram of the input array
  for i in arr:
    if i not in pair_ht:
      pair_ht[i] = 0
    pair_ht[i] += 1
    
  for i in arr:
    if k-i in pair_ht:
      total_pairs += pair_ht[k-i]
    if i == k/2:
      total_pairs -= 1
  
  return total_pairs/2


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  k_3 = 6
  arr_3 = [1000000000, 500000000, 500000000, 3, 3]
  expected_3 = 1
  output_3 = numberOfWays(arr_3, k_3)
  check(expected_3, output_3)
  
  k_4 = 20
  arr_4 = [20//2] * 100000
  expected_4 = (100000 * (100000-1))//2
  output_4 = numberOfWays(arr_4, k_4)
  check(expected_4, output_4)  
  
  k_4 = 11
  arr_4 = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
  expected_4 = 9
  output_4 = numberOfWays(arr_4, k_4)
  check(expected_4, output_4)  
  