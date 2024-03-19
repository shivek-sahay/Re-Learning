def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        j = i - 1
        key = arr[i]
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def bucket_sort(arr):
    sort_parameter = 100 #len(arr)
    # create bucket array
    buckets = [[] for _ in range(sort_parameter+1)]
    
    # manage the bucket to use
    for i in range(len(arr)):
        position = arr[i] // sort_parameter
        buckets[position].append(arr[i])

    # sort the individual buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(x for x in insertion_sort(bucket))
    return sorted_array    
        



input_array = [9, 99, 999, 111, 11, 1]
print(bucket_sort(input_array))
