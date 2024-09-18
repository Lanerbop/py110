# PRACTICE PROBLEM 1

# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# print(sorted(lst))
# print(sorted(lst, reverse=True))

# PRACTICE PROBLEM 2

# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# PRACTICE PROBLEM 3

# def to_str(x):
#     return str(x)

# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort(key=to_str)
# print(lst)
# lst.sort(key=to_str, reverse=True)
# print(lst)

# PRACTICE PROBLEM 4

# books = [
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967',
#     },
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800',
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869',
#     },
# ]

# def published_value(my_dict):
#     return int(my_dict['published'])

# sorted_books = sorted(books, key=published_value)
# print(sorted_books)