from string import ascii_lowercase

letters = set(ascii_lowercase)

def is_pangram(string):
    return letters.issubset(string.lower())
