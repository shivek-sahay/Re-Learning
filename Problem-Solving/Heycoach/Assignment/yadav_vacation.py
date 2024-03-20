"""
Mr. Yadav's Vacation
Rajesh Yadav is a English teacher at school who deceived the school into giving him 'n' days off from the school. Yadav wanted to go to Kerala with his daughters, so he wants to allocate several consecutive days to enjoy the holidays. Since he wants to make the best use of his time thus requiring careful preparation, he will only go for at least 'k' days.

You are given an array 'Weather' containing the weather forecast (That is temperature on the i-th day) in Kerala. Temperature is in degrees. Mr. Yadav was born in Himachal, so he can go on vacation only if the temperature does not rise above 't' degrees throughout his trip. He asks you to help him and count the number of ways to choose vacation dates in Kerala.

Example:

Input: n = 3 , k = 1, t = 15

Weather = [-5,0,-10]

Output: 6

Explanation : 

In this example Mr. Yadav can go on these suitable dates [1], [2], [3], [1, 2], [2, 3], [1, 2, 3] which is equal to 6.

Constraints:

1 ≤ n ≤ 10^5

1 ≤ k ≤ n

−100 ≤ t ≤ 100
"""
class Solution:
    def solve(self, weather, n, k, t):
      valid_ways = 0
    
      # Iterate over the Weather array
      for start in range(n):
          for end in range(start + k - 1, n):
              # print(start,end+1)
              # print(weather[start:end+1])
              if all(temp <= t for temp in weather[start:end+1]):
                  valid_ways += 1
      
      print(valid_ways)
