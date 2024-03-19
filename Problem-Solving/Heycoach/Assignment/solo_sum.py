"""
SOLO SUM
Ramesh is working on a problem given by his teacher, the problem states that he is given an array(say nums),

He has to find such an array (say ans) such that ans[i]=leftsum[i]+rightsum[i]. Help Ramesh to solve the problem. leftsum[i] is the sum of all the elements to the left of index i in the array nums, if there is no such element leftsum[i]=0;

rightsum[i] is the sum of all the elements to the right of index i in the array nums, if there is no such element rightsum[i]=0;

Example 1
Input:
nums = [1, 2, 3, 4, 5]
Output:
[14, 13, 12, 11, 10]
Example 2
Input
nums =[1, 2, -3, 4, -5]
Output:
[-2, -3, 2, -5, 4]
Constraints :
1 <= nums.length <= 1000

-10000 <= nums[i] <= 10000
"""

def left_right_sum(nums):
    ans = [0] * len(nums) 
    for i in range(len(nums)):
      left_array = nums[:i]
      right_array = nums[i+1:]
      # print(left_array, right_array)
      if len(left_array) == 0 : 
        left_sum_array = 0
      else :
        left_sum_array = sum(left_array)
      if len(right_array) == 0 : 
        right_sum_array = 0
      else :
        right_sum_array = sum(right_array)
      total_sum = left_sum_array + right_sum_array
      ans[i] = total_sum
    return ans