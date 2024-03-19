"""
Combine the Books
In the enchanting village of Bookland, there are two mystical bookstores, Alara's Books and Balin's Reads.
Your task is to create a program that combines their inventories into a single sorted list.

Input:
4 4

book enchanted spell wand

ancient dragon magic scroll
Output:
ancient book dragon enchanted magic scroll spell wand

Constraints:
The size of each inventory (n) and (m): 1 ≤ n, m ≤ 10^5

Length of each book title: 1 ≤ length ≤ 100

The inventories are sorted in alphabetical order.
"""


def solve(inventory1, inventory2):
    total_inventory = inventory1 + inventory2
    return sorted(total_inventory)


inventory1 = ['book', 'enchanted', 'spell', 'wand']
inventory2 = ['ancient', 'dragon', 'magic', 'scroll']
print(solve(inventory1, inventory2))