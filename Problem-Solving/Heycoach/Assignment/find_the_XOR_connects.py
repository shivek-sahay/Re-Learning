"""
Find the XOR Connects
You have been given two arrays A,B of sizes n, m respectively. You need to return the total connects in the arrays. A connect is defined as XOR of two elements from different arrays which results in 0.

Example 1:-

Input :

A[ ] = {1,2,3,4,5} ,
B[ ] = {1,2,3,4,5}

Output : 5
Example 2:-

Input : 
A[ ]={1,2,3,4,5} ,
B[ ]={7}

Output : 0
Constraints:

1 <= n,m <= 10^5

1 <= A[i],B[i] <= 10^9
"""

class Solution:
    def solve(self, a, b):
      xor_count = 0
      frequency = {}
      for num in a:
        frequency[num] = frequency.get(num, 0) + 1

      for num in b:
        if num in frequency:
          xor_count += 1
      return xor_count