"""
// Video Link 1: https://www.youtube.com/watch?v=TzeBrDU-JaY
// Video Link 2: https://www.youtube.com/watch?v=0nlPxaC2lTw

Steps of Algorithm:
1. We create a base case i.e len(arr) < 2 then return
2. If that's not the case then we need to split the array in two equal parts.
3. Then we will recursively split the left part of the main array until we hit the base case.
4. After sorting the left side we will recursively split the right part of the main array until we hit the
   base case.
5. We will sort the array's by comparing the elements of left and right arrays.
6. Here the method to sort goes like the following:
    - untill the size of the left and right arrays are equal we loop using while loop
    - check if the first indexed element in left array is less than the first indexed element of right array
    - if it is less then we will update the main array's first index with the value of first element 
      of left array.
    - and increment the index of main array and left array.
    - else case we will consider the right array element to be put in the main array and increment the
      index of the main array and the right array.
    - Now, there could be case when the length of the right and left array are not equal.
    So we will do the following.
    -- Now, we will create a while loop for the index at which we have reached for left array till the length
       of the left array and add those element to the main array as we were doing previously and increment the index
       of the left array.
    -- We can perform the same in case of the right array.
7. The above was the way we will sort and join the left's and right's arrays together.
8. This joined array will be returned from the recursion function calls to the main merge sort function.
9. Hence, finally creating a sorted array in the main array.

Merge Sort Properties
1. Not an In Place Sort Algorithm
2. Uses Divide and Conquer method to distribute into sub arrays
3. Recurssion method is used in this sort function.
4. Stable sorting function.

Time Complexity:- O(nlogn)
Space Complexity:- O(n)
"""

def merge_sort(arr):
    # single element array case
    # Base:
    if len(arr) < 2: return

    #Decomposition:
    mid = int(len(arr) // 2)

    left_array = arr[:mid]
    right_array = arr[mid:]
    
    merge_sort(left_array)
    merge_sort(right_array)
    
    #Recomposition:
    merge_function(arr, left_array, right_array)
    return arr

def merge_function(arr, left_array, right_array):
    i = j = k = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    # If left array still has elements
    while i < len(left_array):
        arr[k] = left_array[i]
        k += 1
        i += 1

    # If right array still has elements
    while j < len(right_array):
        arr[k] = right_array[j]
        k += 1
        j += 1


input_array = [1, 0, 2, 1, 0, 2, 1, 0]
print(merge_sort(input_array))