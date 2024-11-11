def merge(A, B, m, n):
    C = []
    i = j = 0  # Start indices at 0, not 1
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    # If there are remaining elements in A or B, add them to C
    C.extend(A[i:])
    C.extend(B[j:])
    print(f"Merged: {C}")
    return C

def mergesort(arr):
    print(f"Splitting:{arr}")
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l = arr[:mid]  # Left half
    r = arr[mid:]  # Right half
    
    # Recursively sort both halves
    l_sorted = mergesort(l)
    r_sorted = mergesort(r)
    
    # Merge the two sorted halves
    return merge(l_sorted, r_sorted, len(l_sorted), len(r_sorted))
   

arr = list(map(int, input("Enter the elements of the list: ").split()))
sorted_arr = mergesort(arr)
print("The sorted array is: ", sorted_arr)
