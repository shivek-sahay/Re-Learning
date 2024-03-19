"""
Special Pair of Scores
You are given an array of integers representing the performance scores of n participants in a coding competition. Each participant is assigned a unique score based on their performance, and no two participants have the same score. Your task is to calculate the total number of Special pairs in the list of scores.
A Special pair is defined as a pair of indices (i, j) such that i < j and scores[i] > scores[j].

Sample Input:
6

8 4 2 1 5 3
Output:
10

Constraints:
The number of participants (n): 2 ≤ n ≤ 10^5.
The scores of participants: 1 ≤ score[i] ≤ 10^9. For example, out of the 10 total pairs 3 possible pairs are : (8,4),(8,5),(4,3).
"""

# Solution Approach
"""
Divide: 
    The array is recursively divided into two halves until each subarray contains only one element.
    A single element is always sorted by definition, so no inversions are present.
Conquer: 
    While merging the subarrays, we can find the inversions. An inversion is a pair where the first element
    is greater than the second element. Since the subarrays are sorted, all the remaining elements in the left subarray will
    form an inversion with the element from the right subarray if a right element is placed before a left element during merging.
Combine: 
    As we merge the subarrays back together, we maintain the sorted order and count the inversions. The number of inversions
    indicates the number of Special pairs.
    The key insight is that when we pick an element from the right subarray and move it before the elements of the left subarray,
    it forms an inversion with each of those elements.
    This is because the elements in the left subarray were originally before the element from the right subarray,
    and they are greater than the element from the right subarray (since the subarrays are sorted).

By counting these inversions during the merge step, we can efficiently calculate the total number of Special pairs in the entire array.
This approach is efficient because each level of recursion involves splitting the array in half (which takes linear time),
and then merging the arrays (which also takes linear time).
Since the depth of the recursion is logarithmic relative to the size of the array (because we’re splitting in half each time),
the overall time complexity is O(nlogn).
"""

def inversion_count(arr):
    temp  = [0] * len(arr)
    return _merge_sort(arr, temp, 0, len(arr)-1)

def _merge_sort(arr, temp, left, right):
    inv_count = 0 
    if left < right:
        mid = (left + right) // 2        
        #count inversion in left half
        inv_count += _merge_sort(arr, temp, left, mid)
        #count inversion in right half
        inv_count += _merge_sort(arr, temp, mid+1, right)
        #count inversion while merge the both halfs
        inv_count += merge_function(arr, temp, left, mid, right)
    return inv_count

def merge_function(arr, temp, left, mid, right):
    i, j , k = left, mid+1, left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else :
            temp[k] = arr[j]
            j += 1
            inv_count += (mid - i+1) #inversions
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy back the merged elements to original array.
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp[loop_var]
    return inv_count

arr = [8, 4, 2, 1, 5, 3]
n = 6
print(inversion_count(arr))