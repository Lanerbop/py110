"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

# input: string
# output: a list of substrings from string that are >= 2 characters
# Requirements:
# - Palindromes are case-sensitive
# - Substrings are >= 2 characters
# - Return value should be a list of substrings
# - empty strings return an empty list


# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]