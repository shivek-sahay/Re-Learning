"""
Detecting Looping Numbers
In this problem, you are tasked with determining whether a given number is a "looping number." A looping number is defined by the following process:


1. Start with any positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
4. If, at any stage of this process, the number forms a cycle that includes 1, it is deemed a looping number. Your objective is to create a function that accepts an integer as input and returns true if it becomes a looping number by reaching 1, and false otherwise.

For example:
1. A number like 23 is a looping number because the process

(2^2 + 3^2 = 13, 1^2 + 3^2 = 10, 1^2 + 0^2 = 1) eventually reaches 1.

2. A number like 4 is not a looping number because it enters a cycle
(4^2 = 16, 1^2 + 6^2 = 37, 3^2 + 7^2 = 58, 5^2 + 8^2 = 89, 8^2 + 9^2 = 145, 1^2 + 4^2 + 5^2 = 42, 4^2 + 2^2 = 20, 2^2 + 0^2 = 4) that does not include 1.

The challenge is to identify whether a given number will continue indefinitely in a cycle or eventually reach the number 1.

Input:
A single integer n.

Output:
Return true if n is a looping number, and false if not.

Example 1:
Input:
n = 23

Output:
true

Example 2:
Input: n = 4 n n n
Output:
true

Constraints:
1 <= n <= 2^31 - 1
Your task is to implement the function isLoopingNumber(n) which will check for the looping number property for the given input n.
"""

class Solution:
    def is_looping_number(self, n): 
      # Set to store visited numbers
      visited = set()
  
      while n != 1:
          # Calculate the sum of squares of digits
          next_n = 0
          while n > 0:
              digit = n % 10
              next_n += digit * digit
              n //= 10
  
          # If we've encountered this number before, it's not a looping number
          if next_n in visited:
              return False
  
          # Add the current number to the visited set
          visited.add(next_n)
          n = next_n
  
      # If we reach here, the number is a looping number
      return True
