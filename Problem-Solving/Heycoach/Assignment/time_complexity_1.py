# class Solution {
#     constructor() {
#         this.cnt = 0;
#     }

#     print() {
#         this.cnt++;
#     }

#     solve(n) {
#       var count = 0 ;
#       for (let i = 0; i < n; i++) {
#         for (let j = i; j >= 0; j--) {
#           for (let k = i; k >= i - 1; k--) {
#             count++;            
#           }
#         }
#       }  
#       console.log(count);
#     }
# }
class Solution:
    def __init__(self):
        self.cnt = 0

    def print(self):
        self.cnt += 1

    def solve(self, n):
      #Write your code here;
      for i in range(0, n):
          for j in range(i, -1, -1):
            for k in range(i, i-2, -1):  
              self.print()

n = 5
solution = Solution()
solution.solve(n)
print(solution.cnt)
