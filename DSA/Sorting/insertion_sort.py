def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            # print(arr)
            # print("\n")
            j -= 1 
        arr[j+1] = key
    return arr

input_array = [4, 5, 10, 15, 20, 16, 25, 7, 1, 6, 9, 2]
print(insertion_sort(input_array))