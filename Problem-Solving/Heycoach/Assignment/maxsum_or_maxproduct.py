class Solution:
    def findans(self, nums):
      s = self.array_sum(nums, 0, len(nums)- 1)
      p = self.array_product(nums, 0, len(nums) - 1)
      if s > p:
          print(1)
      elif s < p:
          print(0)
      else:
          print(-1)
    
    def array_sum(self, nums, left, right):
      #  need to get all the sub array and find their sum to get the final sum
      #  we will be merge sort logic to get the subarray sum
      if left == right:
        return nums[left]

      mid = (left+right) // 2

      return max(self.array_sum(nums, left, mid),
                self.array_sum(nums, mid+1, right),
                self._array_sum_(nums, left, mid, right))
      
    def _array_sum_(self, nums, left, mid, right):
        # Include elements on the left of mid.
        sm = 0
        left_sum = float('-inf')
        for i in range(mid, left-1, -1):
            sm = sm + nums[i]
            if (sm > left_sum):
                left_sum = sm
    
        # Include elements on the right of mid.
        sm = 0
        right_sum = float('-inf')
        for i in range(mid + 1, right + 1):
            sm = sm + nums[i]
            if (sm > right_sum):
                right_sum = sm
    
        # Return sum of elements on the left and right of mid.
        return left_sum + right_sum
    
    def array_product(self, nums, left, right):
      if left == right:
        return nums[left]
      mid = (left + right) // 2

      return max(self.array_product(nums, left, mid),
                 self.array_product(nums, mid+1, right),
                 self._array_product_(nums, left, mid, right)
                )

    def _array_product_(self, nums, left, mid, right):
        # Include elements on the left of mid.
        pr = 1
        left_product = float('-inf')
        for i in range(mid, left-1, -1):
            pr *= nums[i]
            if (pr > left_product):
                left_product = pr
    
        # Include elements on the right of mid.
        pr = 1
        right_product = float('-inf')
        for i in range(mid + 1, right + 1):
            pr *= nums[i]
            if (pr > right_product):
                right_product = pr
    
        # Return product of elements on the left and right of mid.
        return left_product * right_product