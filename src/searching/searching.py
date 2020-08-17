def linear_search(arr, target):
    # Your code here
    length = len(arr) 
    for i in range(length):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, x):
    # Your code here
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) 
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
    # return the value if found
    # return -1 if not found
    return -1  # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
linear_search(arr1, -6)
