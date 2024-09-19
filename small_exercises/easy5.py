# INVERTING DICTIONARY

# Input: Dictionary
# Output: Dictionary w/ keys and values reversed

# Algorithm:
# - initialize empty result dictionary
# - for each item in given dictionary
#   - intialize result[value] = key
# - return result

# def invert_dict(given_dict):
#     result = {}
#     for key, value in given_dict.items():
#         result[value] = key
#     return result

# def invert_dict(given_dict):
#     return {value: key for key, value in given_dict.items()}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

# RETAIN SPECIFIC KEYS

# Input: dictionary and list of keys
# Output: dictionary w items that correspond to keys

# Algorithm
# - create dictionary comprehension
# - loop through key, value in given dict items
# - filtering statement of if key in given keys
# - return comprehension

# def keep_keys(my_dict, keys_list):
#     return {key: value
#             for key, value in my_dict.items()
#             if key in keys_list}

# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

# DELETE VOWELS

# VOWELS = "aeiouAEIOU"

# def remove_vowels(my_string_list):
#     new_list = []
#     for string in my_string_list:
#         no_vowels = ""
#         for char in string:
#             if char not in VOWELS:
#                 no_vowels += char
#         new_list.append(no_vowels)
#     return new_list

# # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

# HOW LONG ARE YOU

