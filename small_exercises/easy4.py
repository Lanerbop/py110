# ALPHABETICAL NUMBERS

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# MY_DICT = {
#     0: 'zero',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
#     10: 'ten',
#     11: 'eleven',
#     12: 'twelve',
#     13: 'thirteen',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'nineteen',
# }

# def number_string(my_int):
#     return MY_DICT[my_int]

# def alphabetic_number_sort(my_ints):
#     return sorted(my_ints, key=number_string)

# print(alphabetic_number_sort(input_list) == expected_result)

# MERGE SETS

# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]

# def merge_sets(lst1, lst2):
#     return set(lst1) | set(lst2)

# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})

# IMMUTABLE INTERSECTION

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})

# def intersection(lst1, lst2):
#     return frozenset(lst1) & frozenset(lst2)
# print(intersection(list1, list2) == expected_result)

# ARRANGE A DICTIONARY -> hard
# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']

# def value_of_key(item):
#     return item[1]

# def order_by_value(some_dict):
#     sorted_items = sorted(some_dict.items(), key=value_of_key)
#     return [key for key, value in sorted_items]

# print(order_by_value(my_dict) == keys)  # True

# UNIQUE ELEMENTS -> could have been shorter

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]

# def unique_from_first(lst1, lst2):
#     return set(lst1) - set(lst2)

# print(unique_from_first(list1, list2) == {9, 3})

# LEADING SUBSTRINGS

# Input: string
# Output: List of all substrings in string starting from 1st char

# Data Structure: List

# Algorithm
# - create an empty substring variable
# - create an empty result list
# - iterate through characters in string
#   - for each iteration, add character to substring
#   - add substring to result list
# - return result list

# def leading_substrings(my_string):
#     my_substring = ""
#     result = []
#     for char in my_string:
#         my_substring += char
#         result.append(my_substring)
#     return result

def leading_substrings(my_string):
    return [my_string[:idx + 1] for idx in range(len(my_string))]

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# ALL SUBSTRINGS

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

def substrings(my_string):
    result = []
    for index in range(len(my_string)):
        result.extend(leading_substrings(my_string[index:]))
    return result

# print(substrings('abcde') == expected_result)  # True

# PALINDROMIC SUBSTRINGS

# def palindromes(my_string):
#     return [substring for substring in substrings(my_string)
#             if substring == substring[::-1] and len(substring) > 1]

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

# INVENTORY ITEM TRANSACTIONS

# Input: Inventory item ID and a list of transactions
# Output: List contraining transactions for item

# Data Structure:
# - Lists
# - Dictionaries

# Algorithm:
# - create empty result transaction list
# - go through each dictionary in list
#   - for each iteration, check if dict['id'] = given id
#   - if true, add dict to result list
# - return result list

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

# def transactions_for(item_id, transactions_list):
#     result = []
#     for my_dict in transactions_list:
#         if my_dict['id'] == item_id:
#             result.append(my_dict)
#     return result

def transactions_for(item_id, transactions_list):
    return [my_dict
            for my_dict in transactions_list
            if my_dict['id'] == item_id]

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

# INVENTORY ITEM AVAILABILITY

# Input: Item Id and transactions list
# Output: boolean true if item available, false else

# Algorithm:
# - get list of transactions for given item id
# - initialize current_quant as 0
# - loop through each dictionary item
#   - if dictionary['movement'] == in:
#     - current_quant += dictionary['quantity']
#   - do opposite for movement out
# - return boolean expression current_quant > 0

# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# def is_item_available(item_id, transaction_list):
#     item_transactions = transactions_for(item_id, transaction_list)
#     current_quantity = 0
#     for transaction in item_transactions:
#         if transaction['movement'] == 'in':
#             current_quantity += transaction['quantity']
#         else:
#             current_quantity -= transaction['quantity']
#     return current_quantity > 0

# print(is_item_available(101, transactions) == False)  # True
# print(is_item_available(103, transactions) == False)  # True
# print(is_item_available(105, transactions) == True)   # True