#tc: wc, ac: O(logn) and bc: o(1)
def binary(array, target):
    left, right = 0, len(array) - 1
    pass_num = 1  # To track each pass

    while left <= right:
        mid = (left + right) // 2
        print(f"Pass {pass_num}: Left = {left}, Right = {right}, Mid = {mid}, Mid Value = {array[mid]}")
        
        if array[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        elif array[mid] < target:
            left = mid + 1
            print(f"Target is greater than {array[mid]}, moving left pointer to {left}")
        else:
            right = mid - 1
            print(f"Target is less than {array[mid]}, moving right pointer to {right}")
        
        pass_num += 1

    print(f"Target {target} not found in the array.")
    return -1

# Taking user input for the array and target value
array = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the target number to search for: "))

# Perform binary search and print the result
result = binary(array, target)
if result != -1:
    print(f"Target {target} is at index {result}.")
else:
    print(f"Target {target} is not present in the array.")
