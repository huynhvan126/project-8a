# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/12/2024
# Description: counts only the letter in a string including upper-case and lower-case letters.
def count_letters(string):
    """Count the number of letters in a string."""
    letter_counts = {}
    for char in string:
        if char.isalpha():
            char = char.upper()
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts
