# CUTE ANGLES -> this was bad

# Input: float representing an angle btwn 0 and 360 deg
# Output: String representing angle in degrees, min, sec

# Test Cases:
# - 30 == "30deg00minutes00seconds"
# - 76.73 == "76deg43minutes48seconds"

# Data Structure
# - floats
# - convert to a string

# Algorithm
# - Calculate degrees and such
#   - use integer division on input to get whole int = my_deg
#   - use modulo 1 * 100 // 1 on initial integer to isolate the total minute value
#   - use total minute value * 3 / 5 to get messy minute value
#   - use messy minute value // 1 to get final minute value as int
#   - use messy minute value % 1 * 100 // 1 to get second value
# - turn results into a string
# - concatenate each result using string interpolation
# - return result

# DEGREE = "\u00B0"
# MINUTES_PER_DEGREE = 60
# SECONDS_PER_MINUTE = 60
# SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

# def dms(degrees_float):
#     degrees_int = int(degrees_float)
#     minutes_int = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
#     seconds = int((degrees_float - degrees_int - (minutes_int / MINUTES_PER_DEGREE))
#                   * SECONDS_PER_DEGREE)
#     result = f"{degrees_int}{DEGREE}{minutes_int:02}'{seconds:02}\""
#     return result

# # All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# COMBINING LISTS

# Input: two lists
# Output: Set of the union of the elements

# Data Structure
# - Sets

# Algorithm
# Use the set constructor function on each list
# return the union of each list

# def union(lst1, lst2):
#     return set(lst1) | set(lst2)

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# HALVSIES

# Input: 1 list
# Output: 1 list w/ 2 elements, 1 list with first half of list, 2nd list with back

# Data Structure
# - Lists

# Algorithm
# - create a result list = [[], []]
# - find the midpoint using the round function
# - use first for loop to iterate through intial_list[:midpoint + 1]
#   - result[0].append the value
# - use second for loop to iterate through intial_list[midpoint + 1:]
# - result[1].append the values
# - return the result list

# def halvsies(my_list):
#     result = [[], []]
#     if len(my_list) % 2 == 0:
#         midpoint_index = round(len(my_list) / 2) - 1
#     else:
#         midpoint_index = round(len(my_list) / 2)

#     for element in my_list[:midpoint_index + 1]:
#         result[0].append(element)
#     for element in my_list[midpoint_index + 1:]:
#         result[1].append(element)
#     return result

# # All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# FIND THE DUPLICATE

# Input: list with a duplicate value
# Output: the duplicate value

# Data Structure
# - Lists

# Algorithm
# - use a for loop to iterate through the list using enumerate
#   - for each iteration check if element is in list - list[current_index]
#   - if true, return element

# def find_dup(lst):
#     for element in lst:
#         lst.remove(element)
#         if element in lst:
#             return element\

# def find_dup(lst):
#     duplicate = [element for element in lst if lst.count(element) == 2]
#     return duplicate[0]

# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

# COMBINE TWO LISTS

# Input: two lists
# Output: 1 list with alternating elements

# Data Structure
# - Lists

# Algorithm
# - create result list
# - zip the lists
# - iterate through zipped lists using elem1, elem2
#   - for each iteration, append elem 1 then append elem 2
# - return result

# def interleave(lst1, lst2):
#     result = []
#     zipped = zip(lst1, lst2)
#     for elem1, elem2 in zipped:
#         result.append(elem1)
#         result.append(elem2)
#     return result

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

# MULTIPLICATIVE AVERAGE

# Input: A list of positive integers
# Output: Average of all given integers

# Data Structure
# - List
# - final ds is a string

# Algorithm
# - initialize sum as 0
# - iterate through the list
#   - for each iteration, add integer to the sum
# - create the average variable as sum / len(given_list)
# - return f string with :03 at the end to give average in 3 decimal places

# def multiplicative_average(my_list):
#     product = 1
#     for integer in my_list:
#         product *= integer
#     average = product / len(my_list)
#     return f"{average:.3f}"

# # All of these examples should print True
# # All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# MULTIPLY LISTS

# Input: two lists of the same length containing integers
# Output: one list that contains the product of each pair of numbers w/ same index

# Data Structure
# - lists

# Algorithm
# - zip list1 and list2
# - create an empty result list
# - use a for loop to iterate through zipped list1 and list2
#   - append the value from multiplying first and second element to result
# - return result

# def multiply_list(list1, list2):
#     result = []
#     my_zip = zip(list1, list2)
#     for elem1, elem2 in my_zip:
#         result.append(elem1 * elem2)
#     return result

# use list comprehension

# def multiply_list(list1, list2):
#     return [a * b for a, b in zip(list1, list2)]


# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

# LIST OF DIGITS -> perfect!

# Input: a positive integer
# Output: a list of the digits in the integer

# Data Structure
# - lists

# Algorithm
# - create an empty result list
# - use a for loop to iterate through string of integer
#   - for each iteration, append the integer of the digit to result list
# - return result

# def digit_list(my_int):
#     return [int(digit) for digit in str(my_int)]


# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

# HOW MANY?

# Input: a list containing strings
# Output: Each element along with the number of times that element is in list

# Data Structure
# - lists

# Algorithm
# - create an empty result dictionary
# - use a for loop to iterate through the given list
#   - for each iteration, incremenet the element count by 1
# - loop through dictionary
#   - for each iteration, print key then print count

# def count_occurrences(my_list):
#     result = {}
#     for elem in my_list:
#         result[elem] = result.get(elem, 0) + 1
#     for k, v in result.items():
#         print(f"{k} => {v}")

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

# LIST AVERAGE -> forgot about sum function

# def average(integers):
#     total = sum(integers)
#     return total // len(integers)

# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True

