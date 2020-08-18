"""
Suffix Tree from Suffix Array and LCP Array

# Algorithm
1. Build suffix array and lcp array
2. Start from only root vertex
3. grow first edge for the first suffix
4. for each next suffix, go up from leaf until LCP with previous is below
5. Build a new edge for the new suffix
"""

class TrieNode:
    def __init__(self, parent, children):
        self.parent = parent
        self.children = children

    def __repr__(self, level=0):
        ret = "\t" * level + "Keys: " + " ".join(self.children.keys()) + "\n"
        for child in self.children.values():
            ret += child.__repr__(level+1)
        return ret

def build_suffix_array(s):
    suffixes = []
    for idx in range(len(s)):
        suffixes.append((idx,s[idx:]))
    suffixes.sort(key=lambda x:x[1])
    print(suffixes)
    return [x[0] for x in suffixes]

def build_lcp_array(s, suffix_array):
    # use rank concept, keep track of matches in iteration (h) and use it for next (h-1)
    lcp = [0] * len(s)
    rank = [0] * len(s)
    h = 0
    # build rank (or) inverse array for suffix array
    for i in range(len(s)):
        rank[suffix_array[i]] = i
    for i in range(len(s)):
        # get string position of previous suffix to i
        k = suffix_array[rank[i] - 1]
        while (i+h) < len(s) and (k+h) < len(s) and s[i+h] == s[k+h]:
            h += 1
        lcp[rank[i]] = h
        if h > 0:
            h -= 1
    return lcp

def build_suffix_tree(s, root, suffix_array, lcp_array):
    # Take the first suffix in the suffix array and build a new node and link
    # root and new node

    # First suffix
    first_suffix = s[suffix_array[0]:]
    child = TrieNode(root, {})
    root.children[first_suffix] = child
    current_node = child
    depth = 1

    # Loop through rest of the suffixes and with the help of lcp array, insert
    # the suffixes in the correct depth of the tree
    for i in range(1, len(suffix_array)):
        current_lcp = lcp_array[i]
        current_suffix = s[suffix_array[i]:]
        
        # find the correct place to insert the next node by comparison depth and
        # current_lcp. If depth is greater than lcp, traverse up the tree until
        # they are equal
        while current_lcp < depth:
            current_node = current_node.parent
            depth -= 1
        
        if (current_lcp == 0):
            # if lcp for the current i is 0, there's no common prefix, so create a
            # new node and attach it to the current node.
            child = TrieNode(current_node, {})
            current_node.children[current_suffix] = child
            current_node = child
            depth += 1
        else:
            # if lcp is not 0, we have a common prefix with the current node and
            # suffix i, so create/split the nodes accordingly
            """ Create/Split example when '$' and 'a$' are already in the suffix tree and you get 'aa$' with lcp of 1 in the current loop
                root
                    $
                    a$

                lcp['aa$'] = 1

                root
                    $
                    a --> keep lcp length value in the current node
                        $ --> create a new node and move the rest of the previous nodes letters to this new node, link this with parent
                        a$ --> create another node with lcp removed from the current suffix and link to parent
            """
            # Get all the keys for splitting and creating new nodes
            key_to_split = [k for k,v in current_node.parent.children.items() if v == current_node][0]
            new_child_key_suffix = current_suffix
            previous_suffix = s[suffix_array[i-1]:]
            new_child_key_split = previous_suffix[current_lcp:]            
            new_parent_key_split = key_to_split[ : - len(new_child_key_split)]
            new_child_key_suffix = s[suffix_array[i]+current_lcp : ]

            # remove the old parent key and insert the correct new parent key and link the parent-child nodes
            del current_node.parent.children[key_to_split]
            current_node.parent.children[new_parent_key_split] = current_node

            # Now, create two children - one to hold the key that was split from
            # parent and other that holds the current suffix (with lcp removed)
            # child 1 (split from current)
            child = TrieNode(current_node, {})
            current_node.children[new_child_key_split] = child

            # child 2 (the current suffix with lcp removed)
            child = TrieNode(current_node, {})
            current_node.children[new_child_key_suffix] = child
            current_node = child
            depth += 1


def driver_function():
    s = "banana"
    
    # make sure to add a sentinel to the end of s to ensure suffix tree is not
    # an implicit tree i.e we need exactly N leaf nodes and not at most N leaves
    s += "$"

    suffix_array = build_suffix_array(s) # o(n^2)
    print(suffix_array)

    lcp_array = build_lcp_array(s, suffix_array) # O(n)
    print(lcp_array)

    root = TrieNode(None, {}) # O(n)
    build_suffix_tree(s, root, suffix_array, lcp_array)
    print()
    print(repr(root))

driver_function()
    