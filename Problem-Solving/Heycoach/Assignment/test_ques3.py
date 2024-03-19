class Solution:
    def solve(self, n, a, b):
      #Write your code here
      max_of_a = max(a) # 9
      max_of_b = max(b) # 9
      a_nth_elem = a[n-1] # 7
      b_nth_elem = b[n-1] # 9
      if max_of_a != a_nth_elem:
        # a array need change
        a[n-1] , b[n-1] = b[n-1], a[n-1]         
        
      if max_of_b != b_nth_elem:
        # b array need change
        b[n-1] , a[n-1] = a[n-1], b[n-1]
      # Now, check
      if max(a) == a[n-1] and max(b) == b[n-1]:
         print("YES")
      else:
         print("NO")
 