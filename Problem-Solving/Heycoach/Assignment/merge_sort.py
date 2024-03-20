"""
Merge Sort
In the friendly village of Sortville, there lived a kind wizard named Willy. Willy was known for his love of arranging things neatly. One day, while exploring the forest, he found a box filled with jumbled-up numbers written on colourful pebbles. Willy wanted to put them in order because he thought it would be fun.

Task:
Now, it's your job to help Willy arrange these colourful pebbles in the correct order. Write a program named mergeSort to sort the numbers on the pebbles using this method.

Expected Time Complexity is O(n*log(n))
Input:
An integer n (1 to 100,000), tells you how many pebbles there are.

A list of n numbers, written on the pebbles. Each number is between 1 and 100,000.

Output:
A list of n numbers, the pebbles sorted from the smallest to the biggest.

Input:
4

10 5 3 7

Output:
3 5 7 10
"""

class Solution:
    def merge_sort(self, arr, left, right):
      if len(arr) < 2: return
      mid = int(len(arr)//2)
      left_array = arr[:mid]
      right_array = arr[mid:]
      self.merge_sort(left_array, 0, mid)
      self.merge_sort(right_array, mid, len(arr))

      self.merge_function(arr, left_array, right_array)

    def merge_function(self, arr, left_array, right_array):
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
          if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
          else :
            arr[k] = right_array[j]
            j += 1
          k += 1

        while i < len(left_array):
          arr[k] = left_array[i]
          k += 1
          i += 1

        while j < len(right_array):
          arr[k] = right_array[j]
          k += 1
          j += 1
            
