# # PRACTICE PROBLEM 1

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# # ordinary loop

# # sum = 0
# # for person in munsters.values():
# #     if person['gender'] == 'male':
# #         sum += person['age']
# # print(sum)

# # comprehension

# # ages = [person['age'] for person in munsters.values()
# #                       if person['gender'] == 'male']

# # print(sum(ages))

# # PRACTICE PROBLEM 2 -> didn't know how to do this

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # new_list = [sorted(sublist) for sublist in lst]
# # print(new_list)

# # new_list = []
# # for sublist in lst:
# #     new_list.append(sorted(sublist))
# # print(new_list)

# # PRACTICE PROBLEM 3

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # new_list = []
# # for sublist in lst:
# #     new_list.append(sorted(sublist, key=str))
# # print(new_list)

# # new_list = [sorted(sublist, key=str) for sublist in lst]
# # print(new_list)

# # PRACTICE PROBLEM 4

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# # my_dict = {sublist[0]: sublist[1] for sublist in lst}
# # print(my_dict)

# # PRACTICE PROBLEM 5 -> perfect

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# # def sum_of_odds(my_list):
# #     odd_nums = [num for num in my_list if num % 2 == 1]
# #     return sum(odd_nums)

# # new_list = sorted(lst, key=sum_of_odds)
# # print(new_list)

# # PRACTICE PROBLEM 6 -> great

# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# # new_lst = [{k: v + 1} for my_dict in lst
# #            for k, v in my_dict.items()]
# # print(new_lst)

# # PRACTICE PROBLEM 7

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# # new_list = []
# # for sublist in lst:
# #         new_list.append([elem for elem in sublist if elem % 3 == 0])
# # new_list = [[elem for elem in sublist if elem % 3 == 0]for sublist in lst]
# # print(new_list)

# # PRACTICE PROBLEM 8

# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# # my_list = []
# # for food, value in dict1.items():
# #     if value['type'] == 'fruit':
# #         sublist = []
# #         for elem in value['colors']:
# #             sublist.append(elem.capitalize())
# #         my_list.append(sublist)
# #     if value['type'] == 'vegetable':
# #         my_list.append(value['size'].upper())
# # print(my_list)

# PRACTICE PROBLEM 9

# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def numbers_are_even(my_list):
#     for num in my_list:
#         if num % 2 == 1:
#             return False
#     return True

# new_list = []
# for my_dict in lst:
#     odd_dict = {}
#     for key, value in my_dict.items():
#         if numbers_are_even(value):
#             odd_dict[key] =  value
#     new_list.append(odd_dict)
# print(new_list)

# PRACTICE PROBLEM 10

# import random as r

# UUID_CHARS = "1234567890abcdef"
# UUID_CHARS_DICT = {}
# counter = 1
# for char in UUID_CHARS:
#     UUID_CHARS_DICT[counter] = char
#     counter += 1

# def create_UUID():
#     UUID = ""
#     for counter in range(1, 33):
#         if counter in [9, 14, 19, 24]:
#             UUID += "-"
#         else:
#             UUID += UUID_CHARS_DICT[r.randint(1, 16)]
#     return UUID

# print(create_UUID())

# PRACTICE PROBLEM 11

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# list_of_vowels = []

# for my_list in dict1.values():
#     for my_string in my_list:
#         for char in my_string:
#             if char in "aeiou":
#                 list_of_vowels.append(char)

# list_of_vowels = [char for my_list in dict1.values()
#                   for my_string in my_list
#                   for char in my_string
#                   if char in "aeiou"]

# print(list_of_vowels)