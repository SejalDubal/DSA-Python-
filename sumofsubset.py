# Function to find all combinations that sum up to the target
def find_combinations(arr, n, target):
    # Create a 2D table where dp[i][j] is True if sum j is possible using the first i elements
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
    
    # A sum of 0 is always possible (using an empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Function to print the subsets that make up the target sum
    def print_combinations(i, j, path):
        if i == 0 and j == 0:
            # If we reach the top left corner of the dp table, print the path
            print(path)
            return
        
        if dp[i-1][j]:
            # If the current sum j can be formed without including the current element arr[i-1]
            print_combinations(i - 1, j, path)
        
        if j >= arr[i-1] and dp[i-1][j-arr[i-1]]:
            # If the current sum j can be formed by including the current element arr[i-1]
            print_combinations(i - 1, j - arr[i-1], path + [arr[i-1]])

    # If the target sum is possible, print the combinations
    if dp[n][target]:
        print(f"Combinations of numbers that sum to {target} are:")
        print_combinations(n, target, [])
    else:
        print(f"No combination of numbers sums to {target}")

# User input for Sum of Subset Problem
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
target = int(input("Enter the target sum: "))

n = len(arr)
find_combinations(arr, n, target)
