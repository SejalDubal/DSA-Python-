# O(nlogn), wc: o(n^2)

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
       
        # Print the array state after partitioning
        print(f"Pivot is at index {pi}, value = {arr[pi]}")
        print(f"Array after partitioning: {arr}\n")
        
        # Recursively sort the elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Taking the last element as the pivot
    i = low - 1  # Index of smaller element

    print(f"Starting partition: low = {low}, high = {high}, pivot = {pivot}")

    for j in range(low, high):
        print(f"  Comparing {arr[j]} with pivot {pivot}")
        if arr[j] < pivot:
            i += 1
            # Swap if element is less than the pivot
            arr[i], arr[j] = arr[j], arr[i]
            print(f"  Swapped {arr[i]} and {arr[j]} -> {arr}")
    
    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"  Placing pivot {pivot} at position {i + 1}")
    print(f"Partitioned array: {arr}\n")
    return i + 1

# Taking user input for the array
arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))

# Perform quick sort and print the sorted array
print("Starting Quick Sort...\n")
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")

