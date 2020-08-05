# Listen
# Big enough example
# Brute force approach first if possible and then proceed with optimization
# Algorithm Optimization (BUD)
#   1. BUD - Bottlenecks, Unnecessary Work, Duplicated Work
#   2. Look for space-time tradeoffs

# Find rectangle at origin (0,0) with the biggest sum given a matrix of unsigned
# integers

# Matrix
#  6     5    -9    2
# -2    -5    -2    7
#  3    -2    10    13
# -8    -3     1    -2

matrix =[
    [6, 5, -9, 2],
    [-2, -5, -2, 7],
    [3, -2, 10, 13],
    [-8, -3, 1, -2]
]

# Brute force - O(N^4)
total_sum = {}
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        result = 0
        for i in range(len(matrix)-row):
            for j in range(len(matrix[i])-col):
                result = matrix[i][j] + result

        total_sum[str(i) + ',' + str(j)] = result


# print(total_sum)


# optimization 1 - keep a running total using a hash table 
# O(N^2)
total_sum = {}
previous = 0
max = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        result = matrix[i][j] + previous
        previous = result
        # total_sum[str(i) + ',' + str(j)] = result
        if max < result:
            max = result
            largest_rectangle = "(0,0), ("+ str(i) + "," + str(j) + ")"

print(largest_rectangle)


# 0,0 => 6
# 0,1 => 5 (previous + current)
# 0,2 => -9 