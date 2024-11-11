def bubblesort(arr1):
    n = len(arr1)
    for i in range(n):
        swapped = False
        print(f"Pass {i+1}:")
        for j in range(0, n-i-1):
            print(f"Comparing {arr1[j]} and {arr1[j+1]}")
            if arr1[j] > arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
                swapped= True
                print(f"Swapped {arr1[j+1]} and {arr1[j]}")
            else:
                print("no swapping needed")
        if not swapped:
            print("No swaps in this pass")
            break
        print(f"After pass {i+1}: {arr1}")
    return arr1
arr = list(map(int, input("Enter elements: ").split()))
bubblesort(arr)
print(f"Sorted array: {arr}")

