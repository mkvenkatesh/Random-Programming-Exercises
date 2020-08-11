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
    s_idx = 0
    while s_idx < len(S):
        for p_idx in range(len(P)):
            if S[s_idx] == P[p_idx]:
                s_idx += 1

                if p_idx == len(P) - 1:
                    matches += 1

                if s_idx >= len(S):
                    return matches                
            else:
                s_idx -= p_idx
                break     

        s_idx += 1

    return matches

S = "missisippiisipppappspisipsa"
P = "isip"
print(pattern_match(S, P))
