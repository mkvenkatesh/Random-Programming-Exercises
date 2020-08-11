"""
Find the occurrences of pattern P in string S

Un-optimized naive algorithm

Given a string S = "missisippi", find the occurrences of pattern "isip"

while i < len(S)
    Loop p in P:
        if p matches s[i], increment i
        if p doesn't match s[i], break
    incr i

"""

def pattern_match(S, P):
    matches = 0
    for s_idx in range(len(S)):
        for p_idx in range(len(P)):
            if s_idx + p_idx >= len(S):
                break
            if S[s_idx + p_idx] != P[p_idx]:
                break
        if p_idx == len(P) - 1:
            matches += 1

    return matches

S = "missisippiisipppappspisipsa"
P = "isip"
print(pattern_match(S, P))
