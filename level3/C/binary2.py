# Iterative Binary Search Function

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2 # find the middle (floored)
 
        if arr[mid] < x: #lower (left)
            low = mid + 1
 
        elif arr[mid] > x: #higher(right)
            high = mid - 1
 
        else:              #must be this one!
            return mid
 
    
    return -1 #if low == high it was not found
 
 

data = [1,3,6,8,12,13,16,19,21,24,25,40,45,50]
value_to_find = 12
 
result = binary_search(data, value_to_find)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")