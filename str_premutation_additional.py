# With Base Case and Build, we solve the problem first for a base case (e.g., n
# = 1) and then try to build up from there. When we get to more
# complex/interesting cases (often n = 3 or n = 4), we try to build those using
# the prior solutions.

# Consider a test string abcdefg.
# Case "a" --> {"a"}
# Case "ab" --> {"ab", "ba"} Case "abc" --> ?

# This is the first "interesting" case. If we had the answer to P ("ab"), how
# could we generate P ("abc")? Well, the additional letter is "c," so we can
# just stick c in at every possible point. That is:

# P("abc") => insert "c" into all locations of all strings in P("ab")
# P("abc") => insert "c" into all locations of all strings in {"ab","ba"} 
# P("abc") => merge({"cab", ""acb", "abc"}, {"cba", abca", bac"})
# P("abc") => {"cab", "acb", "abc", "cba", "bca", bac"}

# Now that we understand the pattern, we can develop a general recursive
# algorithm. We generate all permu­tations of a strings1• • •sn by "choppingoff"
# the last character and generating all permutations of s1• • • sn_1. Once we
# have the list of all permutations of s1 • • • sn_1, we iterate through this
# list. For each string in it, we insert Sn into every location of the string.

def permutate(s):
    if len(s) <= 1:
        return [s]
    elif len(s) == 2:
        return [s, s[1] + s[0]]
    else:
        temp = permutate(s[:-1])
        new_temp = []
        for item in temp:
            for i in range(len(item)):
                new_temp.append(item[:i] + s[-1] + item[i:])
            new_temp.append(item + s[-1])
        temp = new_temp
        return temp


s = "abcd"
print(permutate(s))