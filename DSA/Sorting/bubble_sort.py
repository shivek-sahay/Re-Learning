import time

def swap(arr, swap_index, swap_from):
    # swap_index is jisme jaye ga
    # swap_from is jisse jaye ga
    arr[swap_index], arr[swap_from] = arr[swap_from], arr[swap_index]
    
def my_code(arr):
    if len(arr) == 1: return; 
    for j in range(0, len(arr)-1):
        if arr[j] > arr[j+1]:
            swap(arr, j+1, j)
            my_code(arr);   
    return arr
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                 swap(arr, j+1, j)
    return arr

def bubble_sort_reverse(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            if arr[j] > arr[j-1]:
                swap(arr, j-1, j)
    return arr
# arr = [15,4,20,10,5,16,25,7,1,6,9,2]
# arr = [25,20,16,15,10,9,7,6,5,4,2,1]
# arr = [4, 5, 10, 15, 20, 16, 25, 7, 1, 6, 9, 2]
# arr = [7, 2, 8, 9, 5]
arr = [4, 6, 2, 5, 3]

start_time = time.time()
# print(my_code(arr))
bubble_sort(arr)
# print(bubble_sort_reverse(arr))
print("--- %s seconds ---" % (time.time() - start_time))
