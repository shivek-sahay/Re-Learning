"""
Minimum Jumps to reach end
Description:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

• 0 <= j <= nums[i]
• i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Input:
•A list of integers nums (1 <= len(nums) <= 10^4), where each element 0 <= nums[i] <= 1000.

Output:
• Return an integer representing the minimum number of jumps to reach the last index.

Example:
Input:
nums = [2,3,1,1,4]

Output::
2

Explanation:
The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Constraints:
• 1 <= nums.length <= 10^4
• 0 <= nums[i] <= 1000
• It's guaranteed that you can reach nums[n - 1].
"""

class Solution:
    def minJumps(self, nums):
      n = len(nums)
      dp = [float('inf')] * n
      dp[0] = 0
  
      for i in range(1, n):
          for j in range(i):
              if j + nums[j] >= i:
                  dp[i] = min(dp[i], dp[j] + 1)
  
      return dp[n-1]
