# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/22/2024
# Description: counts only the letter in a string including upper-case and lower-case letters.
def count_letters(string):
    """Count the number of letters in a string."""
    letter_counts = {}
    for char in string:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            upper_char = char.upper()
            letter_counts[upper_char] = letter_counts.get(upper_char, 0) + 1
    return letter_counts
