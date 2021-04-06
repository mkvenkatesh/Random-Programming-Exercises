# Question 
#
# Given an array of distinct integer values, count the number of pairs of
# integers that have difference k. For example, given the array {1, 7, 5, 9, 2,
# 12, 3} and the difference k = 2,there are four pairs with difference: (1, 3),
# (3, 5), (5, 7), (7, 9).

# examples
# [1] => 0
# [1 4] => (4-1) = 3 <> K(2)
# [1 4 3] => (1,4) (1,3) (4, 3)
# [1 2 3 5 7 9 12] => 
#   (1,2) (1,3) (1,5) (1,7) (1,9) (1,12)
#   (2,3) (2,5)....(2,12)
#   (3,5)....(3,12)
#   ...
#   (9,12)

# brute force
# outer loop from 0 to n-1
# inner loop from i to n
# find difference betwee a[j] & a[i] and if it equals K, increase count.

# optimize 1
# sort array
# for the inner loop j = i to n
#   check if a[j] <= a[i] + k

# optimize 2
# create a list inverse - O(n)
# loop i through original array
#   check in hash table for [a[i] + k]. If so, count++

import timeit
from timeit import Timer

# o(n^2)
def count_pair_int_k_brute(array, k):     
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] - array[i] == k:
                print(f"{array[i]}, {array[j]}")
                #pass

array = [1, 7, 5, 9, 2, 12, 3]
k = 2
count_pair_int_k_brute(array, k)
print()

# [1 2 3 5 7 9 12]
# O(nlog n+ nk)
def count_pair_int_k_opt1(array, k):
    array.sort()
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] > array[i] + k:
                break
            if array[i] + k == array[j]:
                print(f"{array[i]}, {array[j]}")
                break

count_pair_int_k_opt1(array, k)

print()

# O(n) but space O(n)
array = [1, 9, 5, 7, 2, 12, 3]
def count_pair_int_k_opt2(array, k):
    ht = {}
    for item in array:
        ht[item] = item
    
    for i in range(len(array)):
        if array[i]+k in ht:
            print(f"{array[i]}, {array[i]+k}")
            #pass

count_pair_int_k_opt2(array, k)

# t1 = Timer('count_pair_int_k_brute(array, k)', 'from __main__ import count_pair_int_k_brute, array, k')
# print(t1.timeit())

# t1 = Timer('count_pair_int_k_opt1(array, k)', 'from __main__ import count_pair_int_k_opt1, array, k')
# print(t1.timeit())

# t1 = Timer('count_pair_int_k_opt2(array, k)', 'from __main__ import count_pair_int_k_opt2, array, k')
# print(t1.timeit())