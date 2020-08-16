"""
Longest Common Substring

Suppose we have n strings, how do we find the longest common substring that
appears in at least 2 <= k <= n of the strings

Example Consider n=3 and k=2

s1="abca" s2="bcad" s3="daca" s4...

longest common substring given the constraints is "bca" in s1 and s2

# Algorithm

Using suffix arrays & lcps can solve this problem in linear time equal to the
sum of length of input strings.

s = s1 + '$' + s2 + '#' + s3 + '%' 
s = "abca$bcad#daca%"

# https://www.youtube.com/watch?v=Ic80xQFWevc
Make sure you use unique sentinels when you concatenate the strings and should
be lexicographically less than any characters in string s. This is so that we
avoid intermingling suffixes when building the suffix array. When suffix array
is built, the suffixes with these sentinels will be sorted to the top and the
lcp would be all 0 for it, so we can ignore them in our problem.

Now let's build the suffix array and the lcp array on top of s.

Now if we suppose k = 3 (i.e we need the LCS for any 3 strings), then we need to
get the min lcp where strings of different first sentinels have the same lcp
value. We can achieve this by doing a sliding window on top of the lcp array.

# https://www.youtube.com/watch?v=DTLjHSToxmo
Our sliding window starts of with 1 element of lcp array. Until we meet our
criteria of k = 2 (2 strings of different sentinels), we will increase the
sliding window. Once we satisfy our window requirement, we look at min(lcp) for
that window, ignoring the first value, and store that in our max_lcs variable.
Once we do that, if our window criteria is met we shrink the window from the top
and repeat the procedure

suffix array construction in O(n logn) + O(n)
"""



def get_longest_common_substring(s, k, sentinels):
    suffix_array = build_suffix_array(s)
    lcp_array = build_lcp_from_suffix(s, suffix_array)
    print(suffix_array)
    print(lcp_array)
    lcs = get_lcs_for_k(s, suffix_array, lcp_array, k, sentinels)
    return lcs

def build_suffix_array(s):
    suffixes = []
    for i in range(len(s)):
        suffixes.append((i, s[i:]))

    suffixes.sort(key=lambda x:x[1])
    for i in suffixes:
        print(i)
    return [x[0] for x in suffixes]

def build_lcp_from_suffix(s, suffix_array):
    h = 0
    rank = [0] * len(s)
    lcp = [0] * len(s)

    for i in range(len(s)):
        rank[suffix_array[i]] = i

    for i in range(len(s)):
        if rank[i] > 0:
            k = suffix_array[rank[i] - 1]
            while (i+h) < len(s) and (k+h) < len(s) and s[i+h] == s[k+h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

def get_lcs_for_k(s, suffix_array, lcp_array, k, sentinels):
    # implement sliding window to check for LCS. Sliding window size should
    # match k criteria (i.e. suffixes from k different strings). Sliding window
    # is expanded downwards until this condition is met and then we take the
    # min(lcp) value of that window, ignoring the first value, and then shrink
    # our window once our condition is met. Repeat. Maintain the max lcs length
    # and an array to actually hold the lcs during this process
    window_start = 0
    window_end = 0
    window_lcp = 0
    window_k_match = dict([(x, 0) for x in sentinels])

    lcs_array = []
    max_lcs = 0

    # skip suffixes starting with sentinel characters
    while ord(s[suffix_array[window_start]]) < 48: # 48 is ascii 0
        window_start += 1
        window_end += 1

    # since window_k_match is empty, fill it for the first available window element
    k_key = get_sentinel_for_suffix(s, suffix_array, window_start)
    window_k_match[k_key] += 1

    while window_end < len(suffix_array):
        # check window criteria matches k or not
        # if it matches, find min(lcp) for the window. If min_lcp > max_lcp,
        # clear out lcp_array and store max_lcp = min_lcp
        if (check_k_window_criteria(window_k_match, k)):
            # if window criteria is met, get the min lcp of the current window
            # and see if it's greater than what's stored for max
            window_lcp = min(lcp_array[window_start+1 : window_end+1])
            if window_lcp > max_lcs:
                lcs_array = []
                max_lcs = window_lcp
                lcs_array.append(s[suffix_array[window_end] : (suffix_array[window_end] + max_lcs)])
            
            window_start += 1
            # since we shrunk the window, make sure to decrement the sentinel
            # count for the shrunk window
            k_key = get_sentinel_for_suffix(s, suffix_array, window_start - 1)
            if window_k_match[k_key] > 0:
                window_k_match[k_key] -= 1                    

        else:
            window_end += 1
            # since window expanded, fill our window k criteria hash table for the new suffix
            if window_end < len(s):
                k_key = get_sentinel_for_suffix(s, suffix_array, window_end)
                window_k_match[k_key] += 1

    return lcs_array

def get_sentinel_for_suffix(s, suffix_array, idx):
    for char in s[suffix_array[idx]:]:
        if ord(char) < 48:
            return char

def check_k_window_criteria(window_k_match, k):
    non_zero_sentinels = [k for k in window_k_match.values() if k > 0]
    if len(non_zero_sentinels) == k:
        return True
    
    return False


list_of_strings = ["abca", "bcad", "daca"]
k = 3

full_str = ""
sentinel_ascii_start = 33
sentinels = []
for s in list_of_strings:
    full_str += s + chr(sentinel_ascii_start)
    sentinels.append(chr(sentinel_ascii_start))
    sentinel_ascii_start+=1

print(get_longest_common_substring(full_str, k, sentinels))