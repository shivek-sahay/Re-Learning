"""
All Zeroes End
You are given a set of cards, each having either a number or a symbol. Your task is to rearrange the cards in such a way that all the cards with numbers come first,
followed by the cards with symbols, while maintaining the relative order of numbers and symbols.

Example :

Input:

8

3 2 + 4 * - $ 5

Output:

3  2 4 5 + * - $

Input Format:

The first line of input contains an integer N (1 ≤ N ≤ 10^5), representing the number of cards.
The second line of input contains N space-separated elements, where each element is either a positive integer or a single symbol ('+', '-', '*', '$', etc.).
Output Format:

Output the rearranged set of cards on a single line, separated by spaces.
Constraints :

1 ≤ N ≤ 10^5
"""

class Solution:
    def sort_cards(self, cards):
        #Write your code here
        numbers = [card for card in cards if card.isdigit()]
        symbols = [card for card in cards if not card.isdigit()]
        
        # Combine the numbers and symbols back together
        print (' '.join(numbers + symbols))