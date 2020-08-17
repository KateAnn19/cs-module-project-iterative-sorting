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
# def counting_sort(arr, max_value=None):
#     # Your code here
#     counts = [0] * (max_value + 1)
#     for item in the_list:
#         counts[item] += 1

#     # Overwrite counts to hold the next index an item with
#     # a given value goes. So, counts[4] will now store the index
#     # where the next 4 goes, not the number of 4's our
#     # list has.
#     num_items_before = 0
#     for i, count in enumerate(counts):
#         counts[i] = num_items_before
#         num_items_before += count

#     # Output list to be filled in
#     sorted_list = [None] * len(the_list)

#     # Run through the input list
#     for item in the_list:
        
#         # Place the item in the sorted list
#         sorted_list[ counts[item] ] = item

#         # And, make sure the next item we see with the same value
#         # goes after the one we just placed
#         counts[item] += 1

#     return sorted_list
