"""

Rabin-Karp Algorithm - String pattern matching

Average Time Complexity O(N+M); Worst Case - O(N*M), where N is the length of
input string and M is the length of the pattern to match.

# Algorithm
n = t.length
m = p.length
h = dm-1 mod q
p = 0
t0 = 0
for i = 1 to m
    p = (dp + p[i]) mod q
    t0 = (dt0 + t[i]) mod q
for s = 0 to n - m
    if p = ts
        if p[1.....m] = t[s + 1..... s + m]
            print "pattern found at position" s
    If s < n-m
        ts + 1 = (d (ts - t[s + 1]h) + t[s + m + 1]) mod q

"""

def rabin_karp_string_match(text, pattern):
    mod = 29
    base = 26
    t_len = len(text)
    p_len = len(pattern)
    hp = 0
    ht = 0

    # Find hash of pattern and text[0:len(pattern)]
    # Hp = ((p[0] * base^(p_len-1)) + (p[1] * base^(p_len-2)) + ... + p[p_len-1]) % mod
    # Ht0 = ((t0[0] * base^(t0_len-1)) + (t0[1] * base^(t0_len-2)) + ... + t0[t0_len-1]) % mod
    # Hti (rolling hash) = (((hti-1 - (ti-1 * (base ** (p_len-1))) % mod) * base) + ti) % mod

    for i in range(p_len):
        hp += (ord(pattern[i]) * (base ** (p_len-i-1))) % mod
        ht += (ord(text[i]) * (base ** (p_len-i-1))) % mod

    hp = hp % mod
    ht = ht % mod

    # Loop through each letter in text and match the hash values. If they match,
    # loop through the text to ensure a perfect match on the pattern, if not do
    # a rolling hash by including the next letter in the text string and run the
    # match condition again.
    for i in range(0, t_len - p_len + 1):
        # a spurious hit
        if hp == ht:
            # print("hash collission - spurious hit!")
            if text[i : i+p_len] == pattern:
                return i

        ht = (((ht - (ord(text[i]) * (base ** (p_len-1))) % mod) * base) + ord(text[p_len+i])) % mod


text = "ABCCDDAEFG"
pattern = "CDD"
print(rabin_karp_string_match(text, pattern))