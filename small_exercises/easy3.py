# AFTER MIDNIGHT (PART 1) -> purty good. could use constants for calculation

# Input: An integer representing minutes b/a midnight if -/+
# Ouptut: The time of day in a 24-hour format

# Data Structure:
# - Integers

# Algorithm
# - use an if statement to determine whether to add or sub time
# - if adding, add number % 1440 to minutes. 
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60
# - if subtracting, initialize minutes to 1440 - (int % 1440)
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60

# create conversion function
# - set minutes as parameter
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60
# - return f string {2digthour}:{2digitminute}

# def minutes_to_time(minutes):
#     hours = minutes // 60
#     final_minutes = minutes % 60
#     return f"{hours:02}:{final_minutes:02}"

# def time_of_day(given_minutes):
#     MINUTES_PER_DAY = 1440
#     if given_minutes >= 0:
#         minutes = given_minutes % MINUTES_PER_DAY
#     else:
#         minutes = 1440 - (-given_minutes % MINUTES_PER_DAY)

#     return minutes_to_time(minutes)

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

# AFTER MIDNIGHT (PART 2)

# def after_midnight(time_string):
#     hours = int(time_string[:2])
#     minutes = int(time_string[3:])
#     return (hours * 60 + minutes) % 1440

# def before_midnight(time_string):
#     return (1440 - after_midnight(time_string)) % 1440

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

# DOUBLE CHAR (PART 1)

# Input: string
# Output: String with every character doubled

# Data Structure: 
# - String

# Algorithm:
# - create a list comprehension with each char doubled
# - return list joined

# def repeater(my_string):
#     return "".join([char * 2 for char in my_string])

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

# DOUBLE CHAR (PT 2) -> did not need to use list

# def double_consonants(my_string):
#     VOWELS = 'aeiou'
#     char_list = []
#     for char in my_string:
#         if char.casefold() not in VOWELS and char.isalpha():
#             char_list.append(char * 2)
#         else:
#             char_list.append(char)
#     return "".join(char_list)

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

# REVERSE NUMBER

# def reverse_number(my_int):
#     reversed_num_string = str(my_int)[::-1]
#     return int(reversed_num_string)

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

# COUNTING UP

# Input: Integer
# Output: List containing all integer from 1 to given int inclusive ascending

# Data Structure: List

# def sequence(my_int):
#     result = []
#     for digit in range(1, my_int + 1):
#         result.append(digit)
#     return result

# def sequence(my_int):
#     return list(range(1, my_int + 1))

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

# NAME SWAPPING

# Input: FirstName space LastName
# Output: String of "Lastname, Firstname"

# Data Structure: String

# Algorithm
# - Split original string on  whitespace
# - reverse list using .reverse()
# - join on ", "


# def swap_name(name):
#     name_list = name.split()
#     name_list.reverse()
#     return ", ".join(name_list)

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# SEQUENCE COUNT

# Input: 2 integers: count, starting num
# Output: list with count elements, multiple of element

# Data Structure: List

# Algorithm:
# - create an empty result list
# - use a for loop to iterate from 0 to given count
#   - for each iteration, result[index] = starting_num * (index + 1)
# - return result

# def sequence(count, starting_num):
#     result = []
#     for index in range(0, count):
#         result.append(starting_num * (index + 1))
#     return result

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

# REVERSED LISTS

# Input: List
# Output: Mutated List

# Data Structure: List

# Algorithm
# - create empty result list
# - for loop elem in reversed(given_list)
#   - append each element to result list
# - for loop to index in range(0, len(list))
#   - given_list[index] = result[index]

# def reverse_list(my_list):
#     result = []
#     for elem in reversed(my_list):
#         result.append(elem)
#     for index in range(0, len(my_list)):
#         my_list[index] = result[index]
#     return my_list

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

# MATCHING PARENTHESIS

# Input: String that will have parenthesis
# Output: True if properly balanced parenthesis, else false

# Requirements:
# - must start with open parenthesis
# - each parenthesis must have matching closing parenthesis
# - count of open parenthesis in order must be >= count of closed parenthesis


# Data Structure: Strings

# Algorithm
# - create empty parenthesis string
# - loop through given string
#   - if char is in "()", add to parenthesis string
# - initialize both an open and closed parenthesis count
# - loop through parenthesis string
#   - for each iteration, add count to either open or closed parenthesis
#   - return false is closed counter > open counter at any point
# - return open counter == closed counter

# def is_balanced(my_string):
#     paren_count = 0
#     for char in my_string:
#         if char == "(":
#             paren_count += 1
#         elif char == ")":
#             paren_count -= 1
#         if paren_count < 0:
#             return False
#     return paren_count == 0

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True