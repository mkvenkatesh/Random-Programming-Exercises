"""
Insertion Sort

Worst Case - O(N^2) - n-1 + n-2 + ... 2. 1 = N(N+1)/2
Best Case - O(N)
Space - O(1)

# Algorithm 

Sorting is typically done in-place, by iterating up the array, growing
the sorted list behind it. At each array-position, it checks the value there
against the largest value in the sorted list (which happens to be next to it, in
the previous array-position checked). If larger, it leaves the element in place
and moves to the next. If smaller, it finds the correct position within the
sorted list, shifts all the larger values up to make a space, and inserts into
that correct position. 

"""

def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        key = input_array[i]

        for j in range(i - 1, -1, -1):
            if key < input_array[j]:
                input_array[j+1] = input_array[j]
            else:
                j += 1 # having this condition makes it stable sort. If this is removed and we make line #25 <=, this becomes unstable
        
        input_array[j] = key
    
    return input_array

print(insertion_sort([5, 4, 4, 3, 2, 1]))