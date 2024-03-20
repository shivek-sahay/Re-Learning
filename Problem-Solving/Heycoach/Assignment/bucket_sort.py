"""
Bucket Sort
You are the manager at "Dream Wheels" which is a Car Showroom and there are 'n' number of cars available here.
You read an analysis that customers tend to buy expensive rare cars if they come across them after the common cheaper cars.
Your task is to arrange the cars in the decreasing order of their frequency, cars are represented by a string of characters, if two or more cars have the same number of frequencies sort them lexicographically.

Sample Input:
ssgysyqa

Sample Output:
sssyyagq

Constraints:
1<= n <= 10^5
All characters are lowercase only and are English alphabets.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
      #Write your code here
      max_freq = len(s)
      buckets = [[] for _ in range(max_freq + 1)]

      car_count = {}
      for car in s:
        car_count[car] = car_count.get(car, 0) + 1

      for car, freq in car_count.items():
        buckets[freq].append(car)

      result = []
      for freq in range(max_freq, 0 , -1):
        result.extend(x*freq for x in sorted(buckets[freq]))
        # buckets[freq] = sorted(buckets[freq])

      # print(buckets)
      # print(result)
      return "".join(result)