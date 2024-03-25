"""
Arrange the elements alternatively positve and negative

"""
def partition(arr, low, high):
    i = low - 1

    for j in range(low, high):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1] , arr[high] = arr[high], arr[i+1]
    return i+1;

def solution(arr):
    pivot_index = partition(arr, 0, len(arr)-1)

    # print(arr, pivot_index)
    left_index = 0
    right_index = pivot_index+1

    while right_index < len(arr) and left_index < right_index :
        arr[right_index], arr[left_index] = arr[left_index], arr[right_index]
        right_index += 2
        left_index += 2

    print(arr)    

arr = [-5,-2,3,4,-1,9,-7,-10, 12]
print(solution(arr))    