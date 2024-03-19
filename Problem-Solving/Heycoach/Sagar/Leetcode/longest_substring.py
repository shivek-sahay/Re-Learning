# Longest Substring Without Repeating Characters
# Given a string s, find the length of the lengest substring without repeating characters.
# 
# Example 1: 
# input s = "abcabcbb"
# output 3
# The answer is "abc", with the length of 3


def main(s):
    n  = len(s)
    seen = set()
    max_length = left = right = 0
    while (right < n) :
        # If element is not present, find return the end oiterator
        if not s[right] in seen :
            print('add', s[right])
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
            print("max_length", max_length)
            right += 1
        else :
            print('remove', s[left])
            seen.remove(s[left])
            left += 1
        print(seen)
    return max_length

s = 'ytfabytfyfyffytft'
print(main(s))