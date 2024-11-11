# Function to implement Bellman-Ford algorithm
def bellman_ford(graph, V, source):
    # Step 1: Initialize distances from source to all other vertices as INFINITE
    dist = [float("inf")] * V
    dist[source] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(V - 1):
        for u, v, weight in graph:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Step 3: Check for negative-weight cycles
    for u, v, weight in graph:
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
            print("Graph contains negative weight cycle")
            return None

    # Return the shortest distance array
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
source = int(input("Enter the source vertex: "))

# Running the Bellman-Ford algorithm
result = bellman_ford(graph, V, source)

# Displaying the result
if result:
    print(f"Shortest distances from source vertex {source}:")
    for i in range(V):
        print(f"Vertex {i}: {result[i]}")
