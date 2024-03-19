"""
// Video Link 1: https://www.youtube.com/watch?v=pkkFqlG0Hds
// Video Link 2: https://www.youtube.com/watch?v=GUDLRan2DWM

/*
Step of algorithm
1. We loop through the given array.
2. We take first element and try to find value less than the first element in rest of the array.
3. In rest of the array we try to keep the comparison on till we find the minimum value which
   is less than to the first element.
4. Now, after getting the minimum value we swap the first element with the first element.
5. Repeat the step 3 and 4 for all the elements in the array.

O(n^2) Time Complexity. */
"""
def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        min_index = i
        for j in range(i+1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr, i, min_index)
    return arr

def swap(arr, i, j):
    arr[i] , arr[j] = arr[j], arr[i]

input_array = [4, 5, 10, 15, 20, 16, 25, 7, 1, 6, 9, 2]
print(selection_sort(input_array))