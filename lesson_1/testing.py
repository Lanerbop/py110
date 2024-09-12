# produce = {
#     'apple': 'Fruit',
#     'carrot': 'Vegetable',
#     'pear': 'Fruit',
#     'broccoli': 'Vegetable',
# }

# def select_fruit(dictionary):
#     new_dict = {}
#     for key, value in dictionary.items():
#         if value == 'Fruit':
#             new_dict[key] = value
#     return new_dict

# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

# def double_numbers(numbers_list):
#     for index in range(len(numbers_list)):
#         numbers_list[index] *= 2
#     return numbers_list

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

# my_numbers = [1, 4, 3, 7, 2, 6]

# def double_odd_indexes(numbers):
#     doubled_nums = []

#     for idx in range(len(numbers)):
#         if idx % 2 == 1:
#             doubled_nums.append(numbers[idx] * 2)
#         else:
#             doubled_nums.append(numbers[idx])

#     return doubled_nums

# print(double_odd_indexes(my_numbers))  # [2, 4, 6, 14, 2, 6]

# # not mutated
# print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

def multiply(numbers, multiplier):
    multiplied_nums = []
    for number in numbers:
        multiplied_nums.append(number * multiplier)

    return multiplied_nums