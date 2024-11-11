import heapq

# Function to implement Dijkstra's Algorithm
def dijkstra(graph, V, source):
    # Step 1: Initialize distances from the source to all vertices as infinity
    dist = [float("inf")] * V
    dist[source] = 0  # Distance from source to itself is 0
    
    # Min-heap (priority queue) to get the node with the smallest distance
    min_heap = [(0, source)]  # (distance, vertex)

    while min_heap:
        # Step 2: Extract the vertex with the smallest distance
        current_dist, u = heapq.heappop(min_heap)

        # If the distance is already larger, we continue (not needed to process)
        if current_dist > dist[u]:
            continue
        
        # Step 3: Relax all the adjacent vertices
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))  # Add the updated distance to the heap

    return dist

# Function to take graph input from user
def take_graph_input():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    graph = [[] for _ in range(V)]

    print("Enter edges in the form (u v weight): ")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))  # Add directed edge from u to v with the given weight
        graph[v].append((u, weight))  # For undirected graph, also add reverse edge

    return graph, V

# Taking input from the user
graph, V = take_graph_input()
source = int(input("Enter the source vertex: "))

# Running Dijkstra's algorithm
result = dijkstra(graph, V, source)

# Displaying the result (Shortest distances from the source)
print(f"Shortest distances from source vertex {source}:")
for i in range(V):
    print(f"Vertex {i}: {result[i]}")
