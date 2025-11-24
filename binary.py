def binary_search(array,target):
    left=0
    right = len(array)-1
    mid = 0
    while left <= right:
        mid =(left + right) //2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
array = [12,3,54,67,8,34,7]
target = 54
result = binary_search(array,target)
if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in list1")
    
