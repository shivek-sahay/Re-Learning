"""
Can you move two's?
Given an integer array nums, move all 2's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

You don't need to return anything in the function just perform inplace operations.

Example
Input :
arr = [2,2,1]

Output :
[1,2,2]

Constraints:
1 <= arr.length <= 4 * 10^4

0 <= arr[i] <= 10^9
"""

class Solution:
    def movetwos(self, nums):
      new_position = 0
      for num in nums:
        if num != 2:
          nums[new_position] = num
          new_position += 1
      while new_position < len(nums):
        nums[new_position] = 2
        new_position += 1