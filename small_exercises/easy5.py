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

# Input: String
# Output: list of (word + len(word))

# def word_lengths(my_string=""):
#     if my_string:
#         words = my_string.split()
#         for index, word in enumerate(words):
#             words[index] = f"{word} {len(word)}"
#         return words
#     return []

# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# LIST ELEMENT MULTIPLICATION

# def multiply_items(list1, list2):
#     zipped = zip(list1, list2)
#     return [int_a * int_b for int_a, int_b in zipped]

# def multiply_items(list1, list2):
#     result = []
#     for i in range(len(list1)):
#         result.append(list1[i] * list2[i])
#     return result

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# SUM OF SUMS

# Input: List of numbers
# Output: Sum of first num, second num  to beginning etc

# Algorithm
# - initialize sum as 0
# - for each index from range(len(given list))
#   - add sum(given_list[:index + 1])
# - return sum

# def sum_of_sums(my_nums):
#     total = 0
#     running_total = 0
#     for num in my_nums:
#         running_total += num
#         total += running_total
#     return total

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

# SUM OF DIGITS

# def sum_digits(my_int):
#     total = 0
#     for digit in str(my_int):
#         total += int(digit)
#     return total

# def sum_digits(my_int):
#     my_list = [int(digit) for digit in str(my_int)]
#     return sum(my_list)

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

# STAGGERED CASE (PART 1)

# Input: String
# Output: String with staggered capitalization

# Algorithm
# - create an empty string
# - loop through characters in given string
#   - if character has even index, capitalize
#   - else lowercase
# - return new string

# def staggered_case(my_string):
#     result = ""
#     lower_or_upper = "upper"
#     for char in my_string:
#         if not char.isalpha():
#             result += char
#         elif lower_or_upper == "upper":
#             result += char.upper()
#             lower_or_upper = "lower"
#         else:
#             result += char.lower()
#             lower_or_upper = "upper"
#     return result

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

# REMOVE CONSECUTIVE DUPLICATES

# Input: List of integers
# Output: List of integers with only consecutive dupes removed

# Algorithm
# - create list comprehension
# - get int from idx, int of given list
# - only if given list [idx - 1] == current int

# def unique_sequence(my_list):
#     return [my_int for idx, my_int in enumerate(my_list)
#             if idx == 0 or my_int != my_list[idx - 1]]

# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True