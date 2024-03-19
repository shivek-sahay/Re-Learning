"""
Dutch Flag Problem
You are given an array of colourful balls represented by integers, where each integer can have one of three distinct values: 0 (red), 1 (white), or 2 (blue). Your task is to sort the array in such a way that all the red balls come first, followed by all the white balls, and then all the blue balls, effectively solving the Dutch National Flag problem.

Input Format:

The first line of input contains an integer N (1 ≤ N ≤ 10^5), representing the number of colourful balls in the array.
The second line of input contains N space-separated integers, where each integer is either 0 (red), 1 (white), or 2 (blue).
Output Format:

Output the sorted array of colourful balls on a single line, separated by spaces.

Input:

8

1 0 2 1 0 2 1 0
Output:
0 0 0 1 1 1 2 2
"""

# This can be solved using the partition template

# low, mid, high
# section are
# 1. 0  to low
# 2. low to mid - 1
# 3. mid to high

# Solution Approach
"""
Initialization:
    The low pointer is initialized at the start of the array.
    The mid pointer is initialized at the start of the array.
    The high pointer is initialized at the end of the array.

Processing:
    The mid pointer is used to iterate through the array.
    If the element at mid is 0 (red ball), it belongs at the beginning of the array. Swap the element at mid with the element at low and increment both low and mid.
    If the element at mid is 1 (white ball), it is in the correct position, so just increment mid.
    If the element at mid is 2 (blue ball), it belongs at the end of the array.
    Swap the element at mid with the element at high and decrement high.
    Do not increment mid because the element swapped from high might be 0 or 1 and will need to be evaluated.
Termination:
    The process continues until the mid pointer surpasses the high pointer.
    
The result is that all 0s are moved to the front, all 1s are in the middle, and all 2s are at the end of the array.
This sorting is done in-place, without using extra space for another array, and in linear time, which makes it an efficient solution.

"""

def dutch_problem(arr):
    low, mid, high = 0 , 0 , len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid], arr[low]
            low, mid = low + 1, mid + 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
arr = [1, 0, 2, 1, 0, 2, 1, 0]
print(dutch_problem(arr))



