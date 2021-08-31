# Disjoin sets implementation

# Disjoint sets is a group of sets where no item is in more than one set. It supports two operations
# 1. Find - given a node, it finds the disjoin set it belongs to
# 2. Union(s1, s2) - given two sets, it unions them into one set with s1 added to s2's root

# Disjoint sets can be implemented using a tree or hash table.

class DisjointSets:
    def __init__(self):
        self.parent = {}
        self.rank = {} # set's depth

    def make_init_set(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        if node == self.parent[node]:
            return node
        else:
            return self.find(self.parent[node])

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1

    def print_disjoint_set(self, node):
        if node == self.parent[node]:
            print(node, end='')
        else:            
            self.print_disjoint_set(self.parent[node])
            print(" -> ", node, end='')        


if __name__ == "__main__":
    d = DisjointSets()
    for c in ('a','b','c','d','e'):
        d.make_init_set(c)

    print(d.find('c'))
    d.union('c', 'a')
    d.union('d', 'b')
    print(d.find('c'))
    d.print_disjoint_set('c') # c is pointing to a
    print()
    d.union('a', 'b')
    print(d.find('c'))
    d.print_disjoint_set('c') # c is pointing to a which is pointing to b
    print()