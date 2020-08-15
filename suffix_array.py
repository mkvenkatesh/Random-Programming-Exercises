"""
Suffix Arrays - O(n^2 log n)

A suffix is a non-empty substring at the end of the string. A suffix array
contains all the sorted suffixes of a string

A suffix array provides a space efficient alternative to a suffix tree which
itself is a compressed version of a trie. Suffix array can do something a suffix
tree can, with some additional information such as Longest Common Prefix (LCP)
array. 

A suffix array can be constructed from Suffix tree by doing a DFS traversal of
the suffix tree. In fact Suffix array and suffix tree both can be constructed
from each other in linear time.

Advantages of suffix arrays over suffix trees include improved space
requirements, simpler linear time construction algorithms (e.g., compared to
Ukkonen’s algorithm) and improved cache locality 

"""
# O(n^2 logn) Sorting uses O(nlogn) comparisons, and since comparing two strings
# will additionally take O(n) time, we get the final complexity of O(n2logn).
def suffix_arrays_naive(s): 
    # get all the suffixes of s into an array
    # sort that array
    suffixes = []
    for i in range(len(s)):
        suffixes.append((s[i:], i))
    #print(suffixes)

    suffixes.sort(key=lambda x: x[0]) # O(n^2 log n)
    suffixes = [x[1] for x in suffixes] 
    #print(suffixes)
    return suffixes

suffixes = suffix_arrays_naive("banana")
print(suffixes)