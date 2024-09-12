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

# LETTER SWAP

