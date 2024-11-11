def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index if target is found
    return -1  # Return -1 if target is not found

# Taking user input
arr = list(map(int, input("Enter the elements of the array: ").split()))
target = int(input("Enter the target value to search for: "))

# Performing linear search
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
