"""
GCD of the smallest
You have been given an array of size n. You need to perform certain operations on the array to reduce the size of the array to one according to the following rule:

1). Add two smallest numbers from the array and append the number back to the array.

2). The cost of doing the above operation is equal to GCD (Greatest Common Divisor) of the smallest two numbers in the array.

Return the total cost after the last number is left in the array.

Example:

Input : n = 5  ar =  [5,4,2,3,1]

Output:  8
Constraints:

1 <= n <= 1000

1 <= array[i] <= 1000
"""

class Solution:
    def solve(self, ar):
      sorted_arr = sorted(ar, reverse = True)
      cost = 0
      while len(sorted_arr) > 1:
        first_elem = sorted_arr.pop()
        second_elem = sorted_arr.pop()
        # print(first_elem, second_elem)
        sum = first_elem + second_elem
        sorted_arr.append(sum);
        cost += self.gcd(first_elem, second_elem)
        sorted_arr = sorted(sorted_arr, reverse = True)
      return cost
        
    def gcd(self, first, second):
    
      min_num = min(first, second)
  
      while min_num:
        if first % min_num == 0 and second % min_num == 0:
          break
        min_num -= 1
        
      return min_num
      
    
