"""
Bubble Sort

Anish and Binish are playing a game. They both have to pick 'n' stones of varying sizes with non-duplicates and give their set of stones to the other. They have to sort these stones in increasing order but are allowed to do just one operation on them that is they can swap any adjacent stones with each other.
The one who sorts their set of stones with the least number of swaps wins. You are given two arrays named 'Anish' and 'Binish' representing the size of stones that they have to sort.
Determine the winner of the game.

Note: If the game is a tie print out "Tie".

Sample Input:
5

7 2 8 9 5

4 6 2 5 3
Sample Output:
Anish
Constraints:
1<=n<=1000

1<=s[i]<=10^5
"""

class Solution:
    def game(self, a, b, n):
      #Write your code here;
      anish_sort_count = self.sort(n, a)
      binish_sort_count = self.sort(n, b)
      if anish_sort_count < binish_sort_count :
        print('Anish')
      elif binish_sort_count < anish_sort_count:
        print('Binish')
      else:
        print("Tie")
      
    def sort(self, n, arr):
      count = 0
      for i in range(1, n):
        for j in range(n-1):
          if(arr[j] > arr[j+1]):
            count += 1
            arr[j+1], arr[j] = arr[j], arr[j+1]
      return count;