"""
MAX FREEQUENCY ELEMENTS SUM
Nitin has just joined a heyCoach training program, he has been assigned to solve the following problem,
given an integer array (say nums), he has been asked to provide the sum of the array elements which has 
maximum frequency.

Example 1
Input

nums = [1, 2, 3, 3, 3, 2, 2, 5]
Output:
5

#### Explanation :

only elements 3 & 2 has maximum frequency(3), 

### **Example 2**

Input 
nums = [7,6,5,8,9]

Output: 
35


Constraints:
1<=nums.length<=1000

`For all 0<= i <nums.length, -1000<=nums[i]<=1000 `
"""
def calculate(nums):
    # dictonary is used to maintain the frequency
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_key = max_value = 0
    # print(frequency.items())
    for key, value in frequency.items():
        if max_key == 0 and max_value == 0:
            max_key , max_value = key, value

        elif value > max_value:
            max_value = value
            max_key = key 
        
        elif value == max_value:
            max_key += key
        # print(max_key, max_value)
    return max_key
        


nums = [1, 2, 3, 3, 3, 2, 2, 5]
print(calculate(nums))

