# Minimum spanning tree in a connected bidirectional weighted graph is the
# subgraph with minimum weight that covers all the vertices of the graph

# Kruskal algorithm can be used to get MST of a graph with the help of disjoint sets

# Kruskal Algo steps
# 1. Create a disjoint set for each vertex of the graph
# 2. sort the edges by increasing order of weights
# 3. for each vertex in the sorted edge:
#       if find(v1) != find(v2): # i.e. the two vertexes are disjointed
#           Add (v1,v2) to output
#           union(v1,v2)
# 4. return output


class DisjointedSets:
    def __init__(self):
        self.parent = {}
        self.rank = {}

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

class Kruskal:
    def kruskal(self, vertices, edges):
        # 1. Create a disjointed set for each vertex
        mst_graph = []
        ds = DisjointedSets()
        for v in vertices:
            ds.make_init_set(v)

        # 2. Sort the edges by its weight in ascending order
        edges.sort()

        # 3. for each edge in the sorted edges, check if the pairs that make the edge are in the same set or disjointed
        for e in edges:
            root1 = ds.find(e[1])
            root2 = ds.find(e[2])
            if root1 != root2:
                mst_graph.append((e[1], e[2]))
                ds.union(root1, root2)

        return mst_graph                

if __name__ == "__main__":
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = [
        (2, 'a', 'f'), 
        (4, 'f', 'a'), 
        (2, 'e', 'd'),
        (3, 'd', 'c'),
        (1, 'f', 'c'),
        (6, 'c', 'b'),
        (5, 'f', 'b'),
        (4, 'b', 'a')
        ]
    k = Kruskal()        
    print(k.kruskal(vertices, edges))