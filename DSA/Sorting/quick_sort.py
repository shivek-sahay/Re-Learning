"""
QUICK SORT

Step of algorithm
1. Define the start and end of the array and also pass it in the quick sort function.
2. Now, determine the partition position at which we will break the provided array.
3. We use a partition function for the same. Refer to the below section for more information.
4. Finally we recursively call the quick sort function for the first part that is from the start -> partition index - 1.
   second part is from the partition_index + 1 -> end. 
5. Here we intentionally leave the element at the partition_index as it already been positioned correctly by the
   partition function.
6. Logic goes like: We will swap and make the element before the pivot element less than the pivot and more than the
   pivot element. This is done recursively untill the array start is not less than the end.
   i.e start == end or start > end (wrong values passed to the quick sort function)

Partition Function Logic
1. We will considert he last element as the pivot.
2. Set the partition_index as the start provided.
3. Loop through the array from the start to the end provided.
4. We will check while looping is the element less than the pivot.
5. If yes, then we will swap the two, such that element in the left side of partition_index becomes
   less than the element of the partition_index element.
6. Now, increment the partition_index by 1.
7. After completion of the loop, we will get the partition/arranged array where the 
   element less than the pivot is located at the left side of partition_index and vice versa.
8. Lastly, we will position the pivot element at the position of the partition_index.
9. Return the partition_index value, that is the index of the pivot element.    
"""
from random import randint

def quick_sort(arr, start, end):
    if start < end:
        partition_index = random_partition_func(arr, start, end)
        quick_sort(arr, start, partition_index - 1)
        quick_sort(arr, partition_index + 1, end)


def partition_func(arr, start, end):
    pivot = arr[end]
    return_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            # here return_index will have greater value than that of i th index.
            # So we will set the i-th index element to the return_index th index element.
            # Such that the element get smaller than the return_index in the left side of the array
            swap(arr, return_index, i)
            return_index += 1
    # At last we add the pivot element to the return_index position
    swap(arr, end, return_index)
    return return_index

def random_partition_func(arr, start, end):
    pivot_index = randint(start, end)
    swap(arr, end, pivot_index)
    return partition_func(arr,start,end)

def swap(arr, i, j):
    arr[i] , arr[j] = arr[j], arr[i]

arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)