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

def get_lcp_from_suffix_array(s, suffixes):
    # 1. get the inverse of suffixes to easily get the predecessor of a given
    # suffix array position
    # 2. loop from 0 to len(s) of the string and for each suffix at i'th
    #    position, get its predecessors and find lcp
    # 3. store this lcp in an array for the suffix order position and decrement
    #    this value by 1 and store as h
    # 4. in the next loop, we will do the same as above, except skimp lcp char
    #    comparison by h for both suffixes.

    h = 0
    rank = [0] * len(s)
    lcp = [0] * len(s)

    # Build the inverse array for suffix array i.e rank array
    for i in range(len(s)):
        rank[suffixes[i]] = i

    # loop through s to find the suffix at i and its predecessor for lcp comparison
    for i in range(len(s)):
        # 0th rank in the suffix array will not have a predecessor, so skip it.
        if rank[i] > 0:
            # get the position in the string s for the predecessor in suffix
            # array for a string with position i
            k = suffixes[rank[i] - 1]

            # do lcp comparison character by character and increment h for any
            # matches
            while ((i+h) < len(s)) and ((k+h) < len(s)) and s[i+h] == s[k+h]:
                h += 1
            
            # set h as the lcp value for the suffix index in suffix array that
            # starts with position i in s
            lcp[rank[i]] = h

            # decrement h by 1 for the next iteration. This is because we remove
            # one character from string s in our next loop so due the suffix
            # array property, the next lcp will have to be >= current lcp -1
            if h > 0:
                h -= 1
    
    return lcp

s = "banana"
suffixes = suffix_arrays_naive("banana")
lcp = get_lcp_from_suffix_array(s, suffixes)

print(suffixes)
print(lcp)