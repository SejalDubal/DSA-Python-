#tc is order of n^2.
def insertsort(arr):
    for i in range (1,len(arr)):
        j = i-1
        X = arr[i]
        while j >= 0 and arr[j] > X:
          arr[j+1] = arr[j]
          j -= 1

        arr[j + 1] = X
        print(f"Pass{i}: {arr}")
    return arr
n = list(map(int,input("Enter the number of elements or arr: ").split()))
arr = list(map(int, input("enter the elements of array to be sorted: ").split()))
print("sorting steps: ")
sorted_arr = insertsort(arr)
print("The sorted array is: ",sorted_arr)




    