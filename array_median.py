def find_median_sorted_arrays(arr1, arr2):
    # Merging the two arrays
    merged_array = sorted(arr1 + arr2)
    length = len(merged_array)
    
    # Finding the median
    if length % 2 == 0:
        median = (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2
    else:
        median = merged_array[length // 2]
    
    return median

# Taking user input
arr1 = list(map(int, input("Enter elements of the first sorted array: ").split()))
arr2 = list(map(int, input("Enter elements of the second sorted array: ").split()))

# Finding the median
median = find_median_sorted_arrays(arr1, arr2)
print(f"The median of the merged array is: {median}")
