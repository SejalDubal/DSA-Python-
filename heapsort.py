# tc: o(nlogn)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Print the initial state of the heap at the beginning of each call to heapify
    print(f"Heapifying at index {i}, array: {arr}")

    # See if the left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        print(f"Swapping {arr[i]} and {arr[largest]} to maintain heap property")
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    print("Building the max heap:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Max heap after heapifying index {i}: {arr}")

    # One by one extract elements
    print("\nSorting the array using heap sort:")
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        print(f"Swapping root {arr[0]} with element {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Array after moving max element to index {i}: {arr}")

        # Call heapify on the reduced heap
        heapify(arr, i, 0)
        print(f"Heap after heapifying root: {arr}\n")

    return arr

# Taking user input for the array
arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))

# Perform heap sort and print the sorted array
print("\nStarting Heap Sort...\n")
sorted_array = heap_sort(arr)
print(f"Sorted array: {sorted_array}")
