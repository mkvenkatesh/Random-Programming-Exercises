"""
DFS - Depth-First Search

"""

class RandomTree:
    def __init__(self, children, value):
        self.children = children
        self.value = value
    
    def __repr__(self, level=0):
        ret = "\t" * level + "Node Value: " + str(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

def dfs_recursive(node):
    if node == []:
        return
    else:
        print(f"Node Value: {node.value}")
        for child in node.children:
            dfs_recursive(child)

def dfs_iterative(node):
    to_visit = []
    to_visit.append(node)

    while to_visit != []:
        visited = to_visit.pop(0)
        print(f"Node Value: {visited.value}")
        to_visit = visited.children + to_visit

# driver code
l2_n1 = RandomTree([], 1)
l2_n2 = RandomTree([], 5)
l2_n3 = RandomTree([], 76)
l2_n4 = RandomTree([], 56)

l1_n1 = RandomTree([l2_n1, l2_n2], 21)
l1_n2 = RandomTree([l2_n3], 23)
l1_n3 = RandomTree([l2_n4], 90)

root = RandomTree([l1_n1, l1_n2], 25)

# print("\n" + repr(root))
print("\n***** DFS Recursive *****")
dfs_recursive(root)

print("\n***** DFS Iterative *****")
dfs_iterative(root)
