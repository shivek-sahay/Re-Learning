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