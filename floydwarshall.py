# Function to implement Floyd-Warshall algorithm
def floyd_warshall(graph, V):
    # Initialize the distance matrix with the given graph values
    dist = [[float("inf")] * V for _ in range(V)]
    
    # Set the distance to 0 for all nodes to themselves
    for i in range(V):
        dist[i][i] = 0
    
    # Initialize distances using the graph input
    for u, v, weight in graph:
        dist[u][v] = weight
    
    # Dynamic Programming approach
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Check if the path from i to j through k is shorter
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Function to take graph input from user
def take_graph_input():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    graph = []

    print("Enter edges in the form (u v weight): ")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        graph.append((u, v, weight))

    return graph, V

# Taking input from the user
graph, V = take_graph_input()

# Running the Floyd-Warshall algorithm
result = floyd_warshall(graph, V)

# Displaying the result (Shortest paths matrix)
print("\nShortest distances between every pair of vertices:")
for i in range(V):
    for j in range(V):
        if result[i][j] == float("inf"):
            print(f"INF", end=" ")
        else:
            print(result[i][j], end=" ")
    print()
