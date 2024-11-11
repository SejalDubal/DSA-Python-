def find_max_min(arr, low, high):
    # If there's only one element
    if low == high:
        return arr[low], arr[low]
    
    # If there are two elements
    if high == low + 1:
        return max(arr[low], arr[high]), min(arr[low], arr[high])
    
    # Divide the array into two halves
    mid = (low + high) // 2
    left_max, left_min = find_max_min(arr, low, mid)
    right_max, right_min = find_max_min(arr, mid + 1, high)
    
    # Combine the results by comparing the maxima and minima from the two halves
    overall_max = max(left_max, right_max)
    overall_min = min(left_min, right_min)
    
    return overall_max, overall_min

def max_min(arr):
    n = len(arr)
    if n == 0:
        return None, None  # Empty array case
    
    return find_max_min(arr, 0, n - 1)

# User input for the array
arr = list(map(int, input("Enter the elements of the array: ").split()))

# Finding max and min
maximum, minimum = max_min(arr)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
