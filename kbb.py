class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level  # Level in the tree (index of item considered)
        self.profit = profit  # Total profit so far
        self.weight = weight  # Total weight so far
        self.bound = bound  # Upper bound of the profit we can get from the current node

def knapsack_branch_bound(weights, profits, capacity, n):
    # Calculate the upper bound of profit
    def bound(node):
        if node.weight >= capacity:
            return 0
        profit_bound = node.profit
        j = node.level + 1
        total_weight = node.weight

        # Add as much as possible from the next items
        while j < n and total_weight + weights[j] <= capacity:
            total_weight += weights[j]
            profit_bound += profits[j]
            j += 1

        # If there are items left, take fractional part
        if j < n:
            profit_bound += (capacity - total_weight) * profits[j] / weights[j]

        return profit_bound

    # Start with an empty node
    queue = []
    root = Node(-1, 0, 0, 0)
    queue.append(root)

    max_profit = 0
    while queue:
        # Pop node from the queue
        node = queue.pop(0)

        if node.level == n - 1:
            continue

        # Create the next child nodes
        level = node.level + 1

        # First branch: Include the current item
        include_node = Node(level, node.profit + profits[level], node.weight + weights[level], 0)
        if include_node.weight <= capacity:
            include_node.bound = bound(include_node)
            if include_node.bound > max_profit:
                if include_node.profit > max_profit:
                    max_profit = include_node.profit
                queue.append(include_node)

        # Second branch: Exclude the current item
        exclude_node = Node(level, node.profit, node.weight, 0)
        exclude_node.bound = bound(exclude_node)
        if exclude_node.bound > max_profit:
            queue.append(exclude_node)

    return max_profit

# User input for knapsack problem
n = int(input("Enter the number of items: "))
weights = list(map(int, input("Enter the weights of items separated by space: ").split()))
profits = list(map(int, input("Enter the profits of items separated by space: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

# Solve the knapsack problem using branch and bound
max_profit = knapsack_branch_bound(weights, profits, capacity, n)
print(f"The maximum profit that can be obtained is: {max_profit}")
