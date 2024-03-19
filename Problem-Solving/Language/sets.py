# Question: You are given a string, for example "shivek"
# you have to return the no of unique charater you see.
# Here, ans is 6 as unique characters: s h i v e k

# Solution: Whenever there is a mention of uniqueness or
# removal of duplicates, then set is used.

def main():
    #  Step 1: Take the input string
    str = "heycoach"

    # Step 2: Put all the characters inside the set using for loop
    s = set()
    for char in str:
        s.add(char)
    return len(s)

print(main())
