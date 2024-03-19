class Solution:
    def __init__(self):
        self.cnt = 0

    def print(self):
        self.cnt += 1

    def solve(self, n):
      #Write your code here;
        i = n
        while i > 0:
            j = 0
            while j <= i:
                j += 1
                self.print()
            i = int(i / 2)
n = 10
solution = Solution()
solution.solve(n)
print(solution.cnt)