"""
Longest Common Prefix for Suffix Arrays using Kasai's Algorithm

Kasai's algorithm for building a LCP array given a suffix array is O(n), where n
is the length of pattern.

Suffix array will be built below using naive algorithm (O(n^2 log n)) to create
it faster and then LCP using Kasai's will be built on top of it (O(n))

# Algorithm
input: A text S and its suffix array Pos
 1  for i:=0 to n-1 do
 2     Rank[Pos[i]] := i
 3  od
 4  h:=0
 5  for i:=0 to n-1 do
 6    if Rank[i] > 0 then
 7      k := Pos[Rank[i]-1]
 8      while S[i+h] = S[k+h] do
 9        h := h+1
10      od
11      LCP[Rank[i]] := h
12      if h>0 then h := h-1 fi
13    fi
14  od
}

The rank of a suffix is its position in the suffix array, i.e. its rank in the
lexicographic ordering of the suffices. So if Rank[i] = j, then the suffix
starting at the ith position of S is located at position j in the suffix array,
so Pos[j] = i. 

This rank helps us with getting the previous suffix in the suffix array when we
need it for LCP comparison. Once rank array is built, we loop from 0 to
len(s)-1.

Vars: h - represents the number or characters we can skip when comparing the
strings; i is the starting position of suffix1 and k is the starting position
for suffux2 for our lcp comparison.

Steps 
1. We get the rank of suffix starting at length 0 of S i.e Rank[0] which gives
   us the order of this suffix in the suffix array. 
2. We check if this rank > 0, since if it's 0, there's no previous suffix in the
   suffix array. 
3. If rank is not 0, get the previous suffix by doing rank[0] - 1 and then
   getting the position of this suffix in S from the suffix array by doing
   suffix_array[rank[0]-1]. This is our k.
4. We then loop through our string S from i+h to k+h (i.e. get the LCP for the
   two suffixes), we increment h for every character match. This will tell us
   how many characters to skip for LCP comparison on our next iteration
5. once the LCP comparison completes, we store the value of h in a new LCP
   array, that tells the lcp of the suffix in the suffix array i..e lcp[rank[i]]
   = h
6. if h > 0, we decrement h by 1 (this is because we move one position to the
   right of S in our next iteration so we take away one common matched element)
7. Repeat until end of S

Note: When we go from iteration i to iteration i+1, for the suffix in iteration
i+1 the direct predecessor in the suffix array is sandwiched between the suffix
from iteration i+1 and the predecessor from iteration i with the first character
removed. The LCP between the suffix from iteration i+1 and the predecessor from
iteration i with the first character removed is equal to the LCP from iteration
i minus one. Because the predecessor of the suffix in i+1 is sandwiched between
the suffix from iteration i+1 and the predecessor from iteration i with the
first character removed, it follows that the LCP from i+1 is at least the LCP
from i, minus one. Therefore, in the algorithm it is valid to skip the first h
characters when computing the LCP. 
"""

def suffix_arrays_naive(s): 
    suffixes = []
    for i in range(len(s)):
        suffixes.append((s[i:], i))

    suffixes.sort(key=lambda x: x[0])
    print(suffixes)
    suffixes = [x[1] for x in suffixes] 
    return suffixes

def get_lcp(s, suffix_array):
    rank = [0] * len(s)
    for i in range(len(s)):
        rank[suffix_array[i]] = i

    h = 0
    lcp = [0] * len(s)
    for i in range(len(s)):
        if rank[i] > 0:
            k = suffix_array[rank[i] - 1]
            while (i+h < len(s)) and (k+h < len(s)) and (s[i+h] == s[k+h]):
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h = h - 1
    
    return lcp

s = "banana"
suffix_array = suffix_arrays_naive(s)
lcp = get_lcp(s, suffix_array)

print(suffix_array)
print(lcp)