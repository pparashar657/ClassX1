
# len

from curses.ascii import isalnum


str = "Pawan is a good boy"

# print(len(str))

# print(max(str))

# print(min(str))

# ch_arr = sorted(str)

# ch_arr = ['p', 'a', 'w', 'a', 'n']

# ans = ""

# for ch in ch_arr:
#     ans = ans + ch

# print(ans)


# #  string class functions.

# str = "Panwan is a gooD boy"

# # Title fucntion

# print(str.title())

# print(str)

# # Lower

# print(str.lower())

# # upper
# print(str.upper())

# # count

# print(str.count('Pan'))

# print(str.count('a', 4, 11))

# # find

# print(str.find('is'))

# print(str.find('is', 8, 10))

# #  index

# print(str.index('is'))

# print(str.index('is', 8, 10))

# endsWith

# print(str)

# print(str.endswith('a good'))

# startsWith

# print(str.startswith('pawan'))


# a = '10'

# print(type(a[0]))


# str = "Pawan"

# # str = None

# print(str.isalnum())

# print(str.isalpha())

# str = "Pawan123"
# print(str.isalnum())
# print(str.isalpha())

# str = "10"
# print(str.isnumeric())

# str = "paWan "

# print(str.islower())

# str = "ADI"

# print(str.isupper())

# str = "    "

# print(str.isspace())

str = "      Hello World      "

# Strip
print(str.strip())
print(str.lstrip()+"Ok")
print(str.rstrip()+"ok")

# replace

str = "Pawan is a good boy and a good dancer."

print(str.replace("good", "very good"))
print(str.replace("o", "x", 2))

print(str)

# Join

list = ["Pawan", "is", "a", "good", "boy"]

str = ' '.join(list)

print(str)

# split
words = str.split('is')
print(words)
print(type(words))

# partition

part = str.partition(' ')
print(part)
print(type(part))
