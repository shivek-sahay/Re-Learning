"""
// Video Link: https://www.youtube.com/watch?v=Jdtq5uKz-w4

Bubble Sort is the simplest sorting algorithm that works
by repeatedly swapping the adjacent elements if they are
in wrong order. In this we generally find the biggest
element and swap it with the last element.

We can also implement the logic recursively.
Recursive Bubble Sort has no performance advantages, but
can be a good question to check one’s understanding of
Bubble Sort and recursion.

If we take a closer look at Bubble Sort algorithm, we can
notice that in first pass, we move largest element to end
(Assuming sorting in increasing order). In second pass,
we move second largest element to second last position and so on.

Recursive Implementation:
a) Base Case: If array size is 1, return.
b) Do One Pass of normal Bubble Sort.
    This pass fixes last element of current subarray.
c) Recur for all elements except last of current subarray.

Step of algorithm
1. We loop the elements of the array given.
2. We check that if the adjecent element is less than or not.
3. If, less than current element then swap such that we move the greater one towards the end of the array. i.e 0 to n-2
4. So to perfom Step-2 and Step-3 repeatedly, we will loop accross Steps( 2 and 3 ) the elements of the array. i.e 0 to n-1
5. As we can see the largest element of the array is moving towards the end hence that part
   is automatically getting sorted.
6. We can modify the inner loop limit to the 0 to n-i-1 here i is the index of the outer loop.     

Note:- n is the total length of array and range(n) will give us 0 to n-1 loop.

O(n^2) time complexity
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j+1, j)
    return arr

def swap(arr, i, j):
    arr[i] , arr[j] = arr[j], arr[i]

arr = [4, 6, 2, 5, 3]
print(bubble_sort(arr))
