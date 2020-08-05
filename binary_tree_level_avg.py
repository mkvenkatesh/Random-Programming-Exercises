"""
Listen
Example
Brute Force Algo
Optimize (BUD, DIY, Space/Time)
Walkthrough
Code
Test

Given a binary tree, get the average value at each level of the tree

Input:
      4
     / \
    7   9
   / \   \
  10  2   6
       \ 
        6
       /
      2

Output: [4, 8, 6, 6, 2]

Listen/Questions
How is the input provided?
assume it's all integers?
can the input be null nodes?

Example - already given above

Brute Force - explain to interviewer, don't write down
***
Do a Depth First traversal to explore the tree and I can collect all the
numbers by level and you can have this in a has table where the key is the
depth of the tree and it maps to all the numbers at that level. Once I have
this HT, I'll loop though and calculate the avg at each level.
**

Now ask the interviewer if you can start coding with this approach?

"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Dept First Traversal
def avg_by_depth(node):
    dfs_ht = dfs_tree_ht(node)
    results = calculate_avg_ht(dfs_ht)
    return results

def dfs_tree_ht(node, ht = {}, depth = 0):
    if not node:
        return
    else:
        if depth not in ht:
            ht[depth] = (0,0)

        val, count = ht[depth]
        val += node.val
        count += 1
        ht[depth] = (val,count)

        dfs_tree_ht(node.left, ht, depth + 1)
        dfs_tree_ht(node.right, ht, depth + 1)
    
    return ht

def calculate_avg_ht(dfs_ht):
    results = []
    for depth in dfs_ht:
        val, count = dfs_ht[depth]
        avg = int(val/count)
        results.append(avg)
    return results

# Driver code
level5 = Node(2)
level4 = Node(6, level5)
level3_1 = Node(10)
level3_2 = Node(2, None, level4)
level3_3 = Node(6)
level2_1 = Node(7, level3_1, level3_2)
level2_2 = Node(9, level3_3)
root = Node(4, level2_1, level2_2)

avg = avg_by_depth(root)
print(avg)

# BFS traversal
"""
Input:
      4
     / \
    7   9
   / \   \
  10  2   6
       \ 
        6
       /
      2
"""

"""
1. Maintain a queue
2. Add root node to the queue
3. Pop the node off the queue and get all children for that node and push in to queue
4. repeat

0: 4 [7, 9] <- Level 0
1: 7 [9, 10, 2] <- Level 1
2: 9 [10, 2, None, 6] <- Level 1
3: 10 [2, None, 6, None, None] <- Level 2
4: 2 [None, 6, None, None, None, 6] <- Level 2 
5: None [6, None, None, None, 6, None, None] <- Level 2
"""
# recursion
def bfs_traverse(visit):
    if visit == []:
        return
    else:
        popped = visit.pop(0)
        if popped:
            print(popped.val)
            visit.append(popped.left)
            visit.append(popped.right)
        
        bfs_traverse(visit)


bfs_traverse([root])

print("\n\nBFS with Iteration")
# iteration
# 0: [4, None]
# 0: 4 [None, 7, 9]
# 0: None [7, 9, None]
# 1: 7 [9, None, 10, 2]
# 1: 9 [None, 10, 2, 6]
# 1: None [10, 2, 6]
# 2: 10 [2, 6, None]
def bfs_traverse_iter(node):
    if not node:
        return
    else:
        visit = []
        level = 0
        visit.append(node)
        visit.append(None)
        while visit != []:
            popped = visit.pop(0)

            if (popped == None):
                level += 1
                visit.append(None)
                continue
            
            print(popped.val, level)
            if popped.left:
                visit.append(popped.left)
            if popped.right:
                visit.append(popped.right)

bfs_traverse_iter(root)                