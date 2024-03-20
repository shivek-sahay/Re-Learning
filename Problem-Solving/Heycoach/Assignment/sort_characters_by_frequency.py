"""
Sort Characters By Frequency
You are given a string s. Your task is to sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Note:
The task involves sorting a string based on character frequencies. Multiple valid answers exist as characters with the same frequency can be arranged in different orders while still satisfying the requirement.

For example:

Input:
"hello"

Output:
"ollhe" or "olleh" (multiple valid answers)

Input:
"aaaaabbbcccc"

Output:
"ccccbbbbaaaaa"

Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters.

"""

class Solution:
    def frequencySort(self, s):
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        # Sort characters by frequency (and lexicographically if tied)
        sorted_chars = sorted(char_freq.keys(), key=char_freq.get, reverse=True)
    
        # Construct the sorted string
        result = ''.join(char * char_freq[char] for char in sorted_chars)
        return result
