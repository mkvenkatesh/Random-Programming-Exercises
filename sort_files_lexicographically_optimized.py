"""
Sort the Files Lexicographically - Optimized

# Problem 
Your task is given N to return the sorted lexicographically list of file names.
N is in the range [1, 1,000,000]. In 40% of the test cases N will be no higher
than 1,000. If N if higher than 1,000 return just the first 1,000 file names.

SAMPLE INPUT 16

SAMPLE OUTPUT IMG1.jpg IMG10.jpg IMG11.jpg IMG12.jpg IMG13.jpg IMG14.jpg
IMG15.jpg IMG16.jpg IMG2.jpg IMG3.jpg IMG4.jpg IMG5.jpg IMG6.jpg IMG7.jpg
IMG8.jpg IMG9.jpg

# Listen/Questions
# Example
# Algorithm - BruteForce/Bud/Space-Time
# Algo Walkthrough
# Code
# Walkthough
# Test cases

# Algo

Let's say that we need to output the first P files where P = min(N, 1000). The
filenames that come first are the ones starting with IMG1 regardless of the
digits that follow. Next come the ones starting with IMG2, then with IMG3 and so
on.

Among the filenames starting with IMG1 the first is IMG1.jpg, the rest are
sorted according to their second digit and the logic is the same as for ordering
all filenames by the first digit. We should follow this logic to generate the
filenames in the right order.

A recursive implementation could help us here. We could have a method, which is
first called with the prefix IMG and it tries consecutively to attach to it 1,
2, 3, etc. Then it calls itself with IMG1, IMG2, IMG3, etc and does the same
thing. Of course when the number in the filename is higher than N there is not
need to continue as we are only interested in filenames with the numbers in the
range [1, N]. Also, since we generate the filenames in sorted order once we have
generated the first P filenames, we can stop.
"""

import time
start_time = time.time()

def file_sort_lexi(n, result):
    for i in range(1, 10):
        sort_files(result, n, str(i))

def sort_files(result, n, digits):
    if int(digits) > n or len(result) > 1000:
        return
    else:
        result.append("IMG" + digits + ".jpg")
        for i in range(0, 10):
            sort_files(result, n, digits + str(i))
            if int(digits + str(i)) > n:
                break

result = []
file_sort_lexi(10000, result)

print(result)

print("--- %s seconds ---" % (time.time() - start_time))