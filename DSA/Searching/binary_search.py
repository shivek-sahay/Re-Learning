"""
BINARY SEARCH
"""
def binary_search(arr, k, start, end):
    
    if start > end :
        return "Not Found!!"
    middle = (start + end) //2
    
    if arr[middle] == k: return middle

    if arr[middle] > k: return binary_search(arr, k, start, middle -1)
    if arr[middle] < k: return binary_search(arr, k, middle+1, end)


arr = sorted([2, 9, 5, 3, 345, 123, 90, 23, 21, 20])
print(binary_search(arr, 345, start = 0, end = len(arr) - 1))
