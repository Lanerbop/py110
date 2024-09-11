# Problem
# - Input: list of strings
# - Output: new list where strings are sorted based on highest num of adjacent conson
# - Rules:
#   - if two strings have the same highest number, retain original order
#   - consonants are adjacent if next to each other and if there is a space btwn them
#   - Sorted in a descending manner
#   - single consonants are the same as no consonants

# Examples and Test Cases

# ['xxxx', 'xxxb', 'xxxa']

# Data Structures
# - lists
# - dictionaries?

# Algorithm
# 1. For each string in the input list, determine the highest number
#    of adjacent consonants within that string.
# 2. Sort the input list based on the calculated highest number of
#    consonants from step 1.
# 3. Return the sorted list.

# - Remove the spaces from the "input string".
# - Initialize a "maximum consonants count" to zero.
# - Initialize an "adjacent consonants string" to an empty string.
# - For each "letter" in the "input string":
#     - If the "letter" is a consonant:
#         - Concatenate it to the "adjacent consonants string".
#     - If the "letter" is a vowel:
#         - If the "adjacent consonants string" has a length
#           greater than the current "maximum consonants count":
#             - If the "adjacent consonants string" has a length
#               greater than 1:
#                 - Set the "maximum consonants count" to the length
#                   of the "adjacent consonants string".

#         - Reset the "adjacent consonants string" to an empty string.

# - Return the "maximum consonants count".

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(string):
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    max_consonant_count = 0
    string = string.replace(" ", "")
    adjacent_consonants = ""
    for letter in string:
        if letter not in VOWELS:
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonant_count:
                    if len(adjacent_consonants) > 1:
                        max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
            adjacent_consonants = ''
    return max_consonant_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))