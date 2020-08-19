# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range((cur_index + 1), len(arr)):
            if arr[j] < arr[smallest_index]: 
                smallest_index = j
        temp = arr[i] 
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        # TO-DO: swap
        # Your code here
    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Your code here
#     n = len(arr) 
#     # Traverse through all array elements 
#     for i in range(n): 
#         swapped = False
#     # range(n) also work but outer loop will repeat one time more than needed.    
#         # Last i elements are already in place 
#         for j in range(0, n-i-1): 
#             # traverse the array from 0 to n-i-1 
#             # Swap if the element found is greater 
#             # than the next element 
#             if arr[j] > arr[j+1]: 
#                 temp = arr[j]
#                 arr[j] = arr[j+1], 
#                 arr[j+1] = temp
#         if swapped == False:
#             break
#     return arr

def bubble_sort(arr):
    while True:
        swapcount = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1] 
                arr[i + 1] = temp
                swapcount = True
        if swapcount == False:
            return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, max_value=None):
    if len(arr) == 0:
        return []

    if max_value == None:
        max_value = arr[0]
        for j in range(len(arr) - 1):
            if arr[j] < 0:
                return 'Error, negative numbers not allowed in Count Sort'
            if max_value < arr[j]:
                max_value = arr[j]

    print(max_value)
    m = max_value + 1
    count = [0] * m              
    print(count)  
    
    for a in arr:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
    return arr

    return sorted_list

counting_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])