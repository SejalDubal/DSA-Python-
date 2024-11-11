# Disjoint Set (Union-Find) with path compression and union by rank
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's algorithm to find the Minimum Spanning Tree (MST)
def kruskal(n, edges):
    # Sort the edges by weight
    edges.sort(key=lambda edge: edge[2])
    
    # Initialize Disjoint Set for union-find operations
    disjoint_set = DisjointSet(n)
    
    mst = []  # This will store the MST edges
    mst_weight = 0  # This will store the total weight of MST
    
    for u, v, weight in edges:
        # Find the roots of the nodes
        if disjoint_set.find(u) != disjoint_set.find(v):
            # If they are not connected, include this edge in MST
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
    
    return mst, mst_weight

# User input for Kruskal's algorithm
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = []

print("Enter the edges in the format (u, v, weight):")
for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

# Apply Kruskal's algorithm
mst, mst_weight = kruskal(n, edges)

# Output the MST and its weight
print("\nMinimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"Edge: {u} - {v}, Weight: {weight}")
print(f"\nTotal weight of the MST: {mst_weight}")
