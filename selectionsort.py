def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sorting the array
selection_sort(arr)

# Displaying the sorted array
print("Sorted array:", arr)
