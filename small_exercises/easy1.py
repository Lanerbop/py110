# SEARCHING 101 -> could have made print statement shorter

# num1 = input("Enter the 1st number: ")
# num2 = input("Enter the 2nd number: ")
# num3 = input("Enter the 3rd number: ")
# num4 = input("Enter the 4th number: ")
# num5 = input("Enter the 5th number: ")
# num6 = input("Enter the 6th number: ")

# valid_numbers = [num1, num2, num3, num4, num5]
# valid_numbers_string = ", ".join(valid_numbers)

# if num6 in valid_numbers:
#     print(f"{num6} is in {valid_numbers_string}")
# else:
#     print(f"{num6} is not in {valid_numbers_string}")

# PALINDROMIC STRINGS (PART 1)

# Problem
# - Input: string
# - Output: True if string is true palindrome, false otherwise

# Edge/Test Cases
# - Do spaces affect palindrome? -> yes
# - Empty string? -> false

# Data Structure
# - String
# - Boolean return value

# Algorithm
# 1. initialize reversed_string
# 2. return string == reversed_string

# def is_palindrome(txt):
#     reversed_txt = txt[::-1]
#     return txt == reversed_txt

# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

# PALINDROMIC STRINGS (PART 2)

# def is_real_palindrome(txt):
#     txt = txt.casefold()

#     alnum_txt = ""
#     for char in txt:
#         if char.isalnum():
#             alnum_txt += char

#     reversed_alnum_txt = alnum_txt[::-1]
#     return alnum_txt == reversed_alnum_txt

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

# RUNNING TOTALS -> could have done this in an easier way

# Problem
# - Input: List of numbers
# - Output: List of numbers w/ each element being running total from original list

# Edge/Test Cases
# - Empty List? -> Empty List
# - 1 Element list -> Same List
# - Negative Numbers? -> Carry on w/ running total

# Data Structure
# - List w/ integer elements

# Algorithm
# 0. If length of original list == 0 or 1, return the original list
# 1. Initialize the running total list as the first element of original list
# 2. Loop through the original list starting at 2nd element or index 1
# 3. For each iteration, append the value of (running_total[-1] + current int)
# 4. Return the running total list

# def running_total(numbers):
#     if len(numbers) < 2:
#         return numbers
#     else:
#         running_total_list = [numbers[0]]
#         for number in numbers[1:]:
#             running_total_list.append(running_total_list[-1] + number)
#         return running_total_list

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# def running_total(nums):
#     running_total_list = []
#     total = 0

#     for num in nums:
#         total += num
#         running_total_list.append(total)

#     return running_total_list

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# LETTER COUNTER (PART 1) -> pretty good. couldve use more abstraction, but good

# Problem
# - Input: string with zero or more space-separated words
# - Output: dictionary that shows num of words of different {sizes size: count}
# - Requirements:
#   - empty string -> empty dict
#   - word is based on spaces

# Edge/Test Cases
# All of these examples should print True



# Data Type
# - dictionaries
# - strings

# Algorithm
# 1. create a list of the string split on spaces
# 2. create an empty result dictionary
# 3. use a for loop to iterate over each element of the list
# 4. for each iteration, set update the value of the key(length of list)
#    to +1. use get function with 0 argument in case len has not been initialized yet
# 5. return dictionary

# def word_sizes(sentence):
#     alnum_sentence = ""

#     for char in sentence:
#         if char.isalpha() or char == " ":
#             alnum_sentence += char

#     word_list = alnum_sentence.split()
        
#     result = {}

#     for word in word_list:
#         word_size = len(word)
#         result[word_size] = result.get(word_size, 0) + 1

#     return result

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# LETTER SWAP -> correct, could have used helper functin

# Problem
# - Input: String of words separated by spaces
# - Output: String with first and last letters of each word swapped

# Test Cases


# Data Structure
# - Main data structure is a string

# Algorithm
# - Split initial string based on whitespace to get each word in a list
# - Use a for loop to iterate through each word
# - For each iteration, reassign the word with first and last letters switch
#   using slicing and indexing + concatenation
# - return the string joined on a space character

# def swap(my_string):
#     words = my_string.split()
#     result = []

#     for index in range(len(words)):
#         word = words[index]
#         if len(word) == 1:
#             result.append(word)
#         else:
#             result.append(word[-1] + word[1:-1] + word[0])
    
#     return " ".join(result)

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True\

# def swap_first_last_characters(word):
#     if len(word) == 1:
#         return word
    
#     else:
#         return word[-1] + word[1:-1] + word[0]

# def swap(my_string):
#     words = my_string.split()
#     result = []

#     for index in range(len(words)):
#         word = words[index]
#         swapped_word = swap_first_last_characters(word)
#         result.append(swapped_word)
    
#     return " ".join(result)

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# CONVERT A STRING TO A NUMBER -> wrong, used int constructor function

# Problem
# - Input: string of digits
# - Output: digits as an integer
# - Requirements:
#   - No constructor functions

# Test Cases:


# Data Structures
# - Strings

# Algorithm
# - initialize sum variable as 0
# - set tens_multiplier to 0
# - use a while loop for each character/digit in initial string while string true
#   - for each iteration, take modulo 10 to get rightmost digit
#   - add digit * (10**tens_multiplier) to sum
#   - increment tens_multipler by 1
#   - divide num // 10
# - return sum

# def string_to_integer(num_as_string):
#     sum = 0
#     tens_multiplier = 0
#     while num_as_string:
#         digit = num_as_string[-1]
#         sum += int(digit) * (10**tens_multiplier)
#         tens_multiplier += 1
#         num_as_string = num_as_string[:-1]
#     return sum

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

DIGITS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
def string_to_integer(num_as_string):
    sum = 0
    for char in num_as_string:
        sum = (sum * 10) + DIGITS[char]
    return sum

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

# CONVERT A STRING TO A SIGNED NUMBER -> didn't think of match/case

# def string_to_signed_integer(num_as_string):
#     match num_as_string[0]:
#         case '-':
#             return -string_to_integer(num_as_string[1:])
#         case '+':
#             return string_to_integer(num_as_string[1:])
#         case _:
#             return string_to_integer(num_as_string)

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

# CONVERT A NUMBER TO A STRING

# Problem
# - Input: non-negative integer
# - Output: string representing that integer

# Test Cases


# Data Structures
# - strings

# Algorithm
# - create a digits dictionary with integer as key and string as value
# - create an empty result string
# - account for 0
# - use a while loop
#   - extract the rightmost digit using % 10
#   - reassign the string to digits[digit] + current result
#   - divide num // 10
# - return result

DIGITS = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

# def integer_to_string(my_int):
#     result = ""
#     if my_int == 0:
#         return "0"
#     while my_int:
#         digit_int = my_int % 10
#         digit_str = DIGITS[digit_int]
#         result = digit_str + result
#         my_int //= 10
#     return result

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

def integer_to_string(my_int):
    result = ""

    if my_int == 0:
        return "0"
    
    while my_int:
        my_int, digit = divmod(my_int, 10)
        result = DIGITS[digit] + result
    
    return result

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

# CONVERT A SIGNED NUMBER TO A STRING

# def signed_integer_to_string(my_int):
#     if my_int < 0:
#         return "-" + integer_to_string(-my_int)
#     elif my_int > 0:
#         return "+" + integer_to_string(my_int)
#     else:
#         return "0"
    
# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True