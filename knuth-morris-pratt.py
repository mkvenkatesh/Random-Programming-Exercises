"""
Knuth-Morris-Pratt (KMP) Algorithm - String pattern matching

Worst Case - O(n+m) where n is the length of the string and m is the length of
the pattern.

1. Build prefix function using the pattern whose array at q will hold the
longest prefix of pattern p that is a proper suffix of Pq

2. Use this prefix function to backtrack on the pattern during failure when
matching with the string.

"""

def search_pattern_string(s, p):
    pi = build_prefix_function(p)
    match_index = kmp_search(s, p, pi)
    return match_index

def build_prefix_function(p): # O(m) where m is length of pattern p
    # pattern = b a b a b a c b b a
    # pi      = 0 0 1 2 3 4 0 1 1 2
    # maintain two pointers i and j. initially i=0 and j=1 and pi[0] = 0
    # compare i and j
    #   if equal:
    #       set pi[j] = i + 1
    #       increment i and j
    #   else:
    #       if i > 0:
    #           set i = p[i-1]
    #       else:
    #           pi[j] = 0
    #           increment j

    i = 0
    j = 1
    pi = [0] * len(p)
    while j < len(p):
        if p[i] == p[j]:
            pi[j] = i + 1
            i += 1
            j += 1
        else:
            if (i > 0):
                i = pi[i-1]
            else:
                pi[j] = 0
                j += 1
    return pi

def kmp_search(s, p, pi): # O(n) where n is length of string s
    # s  = a b x a b c a b c a b y
    # p  = a b c a b y
    # pi = 0 0 0 1 2 0
    # have one pointer for s (i) and one for p (j), initially they are both 0
    # match s[i] = p[j]
    # if equal:
    #    increment i and j
    # else:
    #     if j > 0:
    #       j = pi[j-1]
    #     else:
    #       increment i

    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p): # match found!
                return i-j
        else:
            if j > 0:
                j = pi[j-1]
            else:
                i += 1

s = "abxabcabcaby"
p = "abcaby"
print(search_pattern_string(s, p))