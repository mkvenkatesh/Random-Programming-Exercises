"""
# Problem

A sequence of numbers is called zigzag sequence if the difference between two
successive numbers strictly alternate between positive and negative.

Fo e.g: 1,7,4,9,2,5 is a zigzag sequence because the difference (6, -3, 5, -7,
3) are alternating between positive or negative

Given a sequence of integers, sequence, return the length of the longest
subsequence of sequence that is zig-zag sequence. A subsequence is obtained by
deleting some number of elements (possibly zero) from the original sequence,
leaving the remaining elements in their original order.


# Questions
1. Would zero break the sequence?
2. Are they all integers?
3. what kind of data structure is the input in? tuple, array, hash table?
4. How long can the input get?
5. What's the range of elements in the sequence?

# Example
Input: 1, 7, 3, 4, 3, 9, 4, 29, 35, 47, 12, 46, 13, 44, 14, 43, 15, 42, 43
Output: 35, 47, 12, 46, 13, 44, 14, 43, 15, 42

# Algorithm
# have a result array and a start/end pointer that you can add to the result array 
# if there's  zigzag sequence
# Loop through each element
#   compare i and i+1 element to see if it's greater, lesser or equal
#   Set start/end/result properly based on the above operations
# Loop through results
#   find the tuple with max length
# return the string sequence between start/end from the max result above
"""

def longest_subsequence_zigzag(sequence): # O(N) + O(M)
    zigzag_indexes = get_zigzag_sequences_index(sequence)
    longest_start_index, longest_end_index = get_longest_subsequence_from_index(zigzag_indexes)
    return sequence[longest_start_index:longest_end_index]

def get_zigzag_sequences_index(sequence):
    results_index = []
    start_index = 0
    end_index = 0
    current_sign = True
    previous_sign = False
    for index in range(len(sequence) - 1): # O(N)
        if (sequence[index] > sequence[index + 1]):
            end_index += 1
            current_sign = False
        elif (sequence[index] < sequence[index + 1]):
            end_index += 1
            current_sign = True
        if (sequence[index] == sequence[index + 1]) or (current_sign == previous_sign):
            results_index.append((start_index, end_index))
            start_index = end_index - 1
        previous_sign = current_sign
    print(results_index)
    return results_index

def get_longest_subsequence_from_index(zigzag_indexes):
    max_length = 0
    longest_index = ()
    for start_end in zigzag_indexes:  # O(M)
        start, end = start_end
        seq_length = end - start
        if (seq_length > max_length):
            max_length = seq_length
            longest_index = start_end
    return longest_index

print(longest_subsequence_zigzag([1, 7, 3, 4, 3, 9, 4, 29, 35, 47, 12, 46, 13, 44, 14, 43, 15, 42, 43]))