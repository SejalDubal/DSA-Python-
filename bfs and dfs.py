from collections import deque

# BFS Implementation
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the start node
    visited.add(start)
    
    while queue:
        node = queue.popleft()  # Remove the element from the front of the queue
        print(node, end=" ")  # Process the node
        
        # Add all unvisited adjacent nodes to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# DFS Implementation (using Recursion)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Process the current node
    print(node, end=" ")
    visited.add(node)
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to take graph input from user
def take_graph_input():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    
    # Take edges as input
    for _ in range(n):
        node = int(input("Enter a node: "))
        neighbors = list(map(int, input(f"Enter the neighbors of node {node} separated by space: ").split()))
        graph[node] = neighbors
    
    return graph

# Take graph input from user
graph = take_graph_input()

# Get the starting node from the user
start_node = int(input("Enter the starting node for BFS and DFS: "))

print("\nBFS traversal starting from node", start_node)
bfs(graph, start_node)

print("\nDFS traversal starting from node", start_node)
dfs(graph, start_node)
