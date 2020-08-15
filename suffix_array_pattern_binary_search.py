"""
Search for pattern in a string using Suffix Arrays - O(m^2 logm) + O(m logn),
where m is the length of pattern and n is the length of input. If we use LCP
array from suffix array, the search can be done in O(m + logn)

If we build a suffix array, we can leverage the sorted property of the suffix
array to quickly find the pattern in the string using binary search

"""

def get_suffix_array(s): 
    suffixes = []
    # generate suffixes
    for i in range(len(s)):
        suffixes.append((i, s[i:]))
    
    # sort suffixes
    suffixes.sort(key=lambda x: x[1])
    return [k[0] for k in suffixes]


def binary_search_pattern(input, pattern, suffix_array):
    # pattern = "nan"
    # input = "banana"
    # suffix_array = [5, 3, 1, 0, 4, 2]

    start = 0
    end = len(suffix_array) - 1

    while start <= end:
        mid = (start + end) // 2

        suffix = input[suffix_array[mid]:]
        if suffix.startswith(pattern):
            return suffix_array[mid]
        elif pattern > suffix:
            start = mid + 1
        elif pattern < suffix:
            end = mid - 1
    
    return -1

def main_program(s, p):
    if p == "":
        return -1

    # O(n*logn) for the sorting and in each sort, we compare up to n characters
    # so total = O(n^2 log n)
    suffix_array = get_suffix_array(s) 

    # O(m logn) for the binary search where m is the length of pattern and n is
    # the length of input i.e it takes log n for binary search and we do m
    # comparisons in each call.
    search_idx = binary_search_pattern(s, p, suffix_array)
    return search_idx

s = "banana"
p = "nan"
print(main_program(s, p))