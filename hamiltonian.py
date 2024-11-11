# Function to check if the current vertex can be added to the Hamiltonian cycle
def is_safe(v, graph, path, pos):
    # Check if this vertex is an adjacent vertex of the last vertex in the path
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included in the path
    if v in path:
        return False

    return True

# Function to solve the Hamiltonian Cycle problem using backtracking
def hamiltonian_cycle_util(graph, path, pos):
    # If all vertices are included in the cycle, return true
    if pos == len(graph):
        # Check if there is an edge from the last vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as the next candidate in the cycle
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            # Recur to construct the rest of the path
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            # Backtrack: Remove the vertex from the path
            path[pos] = -1

    return False

# Function to solve the Hamiltonian Cycle problem
def hamiltonian_cycle(graph):
    path = [-1] * len(graph)  # Initialize the path
    path[0] = 0  # Start from the first vertex

    # Start the backtracking to find the Hamiltonian Cycle
    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian Cycle found")
        return False

    # If a Hamiltonian Cycle is found, print the path
    print("Hamiltonian Cycle found:", path + [path[0]])
    return True

# User input for the graph
n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (1 for edge, 0 for no edge):")
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Check if the Hamiltonian Cycle exists
hamiltonian_cycle(graph)
