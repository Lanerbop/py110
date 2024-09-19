# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
#     counter = decrease(counter)

# print('LAUNCH!')

# def reverse_string(string):
#     new_string = ""
#     for char in string:
#         new_string = char + new_string

#     return new_string

# print(reverse_string("hello") == "olleh")

# def multiply_list(lst):
#     return [elem * 2 for elem in lst]

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

# def get_key_value(my_dict, key):
#     return my_dict.get(key, None)


# print(get_key_value({"a": 1}, "b"))

# events = {
#     "2023-08-13": ["Python debugging exercises"],
#     "2023-08-14": ["Read 'Automate the Boring Stuff'"],
#     "2023-08-15": ["Webinar: Python for Data Science"],
# }

# def is_date_available(date):
#     if date in events:
#         return False

#     return True

# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

# def append_to_list(value, lst=None):
#     if lst == None:
#         lst = []
#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2))

# def multiply_sum(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(multiply_sum(numbers, 2) == 20)

# import copy

# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)

# original[0][0] = 99

# print(copied[0] == [1])

# data_set = {1, 2, 3, 4, 5}

# data_set = {elem for elem in data_set if elem % 2 != 0}

# print(data_set)

# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

# def create_unique_data(my_list):
#     seen = set()
#     result = []
#     for elem in my_list:
#         if elem not in seen:
#             result.append(elem)
#             seen.add(elem)
#     return result

# unique_data = create_unique_data(data)

# print(unique_data == [4, 2, 1, 3]) # order not guaranteed