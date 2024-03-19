"""
Given an integer array a[ ] of length n, you want to create an array res of length 2n where x res[i] == a[i] and res[i + n] == a[n-i-1] for 0 <= i < n (0-indexed).

Hint:
res[ ] array is the concatenation of a[ ] and reverse of a[ ].

Constraints:

1 <= n <= 1000

-1000 <= nums[i] <= 1000
"""

class Solution:
    def reverse_array(self, n, a):
      rev_array = [0]*2*len(a)
      for i in range(len(a)):
        rev_array[i] = a[i]
        rev_array[i+n] = a[n-i-1]
      return rev_array