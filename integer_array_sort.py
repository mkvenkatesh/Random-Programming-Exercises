"""
Problem: Given an array of integers, sort them.

Example: [1, 5, 2, 3, 4, 7, 10, 8] 
Output:  [1, 2, 3, 4, 5, 7, 8, 10]

Questions
1. Can a number repeat?
2. How big is the input?
3. Can it be negative?

# Algorithm - This is called MinSort
# For each element compare it against every other element in the array and swap 
# them if they are greater.
"""

def sort_integer_array(input_array): 
    for num_index in range(len(input_array) - 1):
        for check_index in range(num_index + 1, len(input_array)): # Second iteration (N-1 + N-2 + N-3 ... 2 + 1 0) = N * (N-1)/2
            if input_array[num_index] > input_array[check_index]:
                input_array[num_index], input_array[check_index] = input_array[check_index],  input_array[num_index]
    return input_array

print(sort_integer_array([1, 5, 2, 3, 4, 7, 10, 8]))