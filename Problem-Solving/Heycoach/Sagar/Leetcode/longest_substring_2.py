"""
LongestSubStringWith K unique charachters

Create an algorithm to find a substring with the maximum 
length that contains precisely K distinct characters 
within a given string. 
If multiple substrings have the same maximum length,
 you can output any one of them.

Your Task: You don't need to read input or print anything.
 Your task is to complete the function longestKSubstr() 
 which takes the string S and an integer K as input and
   returns the length of the longest substring with exactly
     K distinct characters. If there is no substring with 
     exactly K distinct characters then return -1.

Sample Input
S = "aabacbebebe", K = 3
Sample Output
7
Explanation
"cbebebe" is the longest substring with 3 distinct characters.
Constraints:
1 <= s.length <= 1e^6
'-a' <= s[i] <= 'z'
K <= 26
"""

def solution(s, k):
    len_s = len(s)

    if k == 0: return -1
    if k > len_s: return -1
    string_freq = {}
    max_length = left = right = 0

    while right < len_s:
        string_freq[s[right]] = string_freq.get(s[right], 0) + 1

        while len(string_freq) > k:
            string_freq[s[left]] -= 1
            if string_freq[s[left]] == 0:
                del string_freq[s[left]]
            left += 1

        if len(string_freq) < k:
           print(string_freq)

        max_length = max(max_length, right - left + 1)
        right += 1
    if len(string_freq) < k : 
        return -1
    else:
        return max_length

s = 'aaabbb'
k = 3
print(solution(s, k))    