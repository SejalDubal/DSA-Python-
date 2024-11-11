# Function to calculate the sum of the search costs (optimal search cost)
def optimal_bst(keys, freq, n):
    # Create a table to store the cost of subtrees
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    # cost[i][i] will store the frequency of the key i
    for i in range(n):
        cost[i][i] = freq[i]
    
    # Calculate the optimal cost for all subtrees of size > 1
    for size in range(2, n + 1):  # Size of the subtree (from 2 to n)
        for i in range(n - size + 1):  # Start index
            j = i + size - 1  # End index
            cost[i][j] = float('inf')
            
            # Try all possible roots for the subtree
            total_freq = sum(freq[i:j+1])  # Sum of frequencies in the range [i, j]
            for r in range(i, j + 1):
                # Calculate the cost of selecting root r and combining left and right subtrees
                left_cost = cost[i][r-1] if r > i else 0
                right_cost = cost[r+1][j] if r < j else 0
                cost[i][j] = min(cost[i][j], left_cost + right_cost + total_freq)
    
    return cost[0][n-1]  # Optimal cost of the entire tree

# User input for OBST
n = int(input("Enter the number of keys: "))
keys = list(map(int, input("Enter the keys separated by space: ").split()))
freq = list(map(int, input("Enter the frequencies of the keys separated by space: ").split()))

print("Optimal search cost of the BST is:", optimal_bst(keys, freq, n))
