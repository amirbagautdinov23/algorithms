def quicksort(arr):
    if len(arr) <= 2:
        return arr
    else:
        pivot = arr[0]
        less = [n for n in arr[1:] if n < pivot]
        greater = [n for n in arr[1:] if n >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

arr = [1,3,4,5,3,7,8,1,2]
arr2= [9,9,1,3,4,5,3,7,8,1,2]

print(quicksort(arr2))
print(sorted(arr2))
print([2] + [3,5,6,1])