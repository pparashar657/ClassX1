
my_dict = {
    "Apple": 100,
    "Orange": 25,
    "Kiwi": 75
}

print('Apples' in my_dict)
print('Apples' not in my_dict)

# Inbuilt functions

print(len(my_dict))

# Class functions:

# Return all keys as list
print(my_dict.keys())

# Return all items as list of tuples of (key, value)

print(my_dict.items())

# Return all values as list

print(my_dict.values())

print(1000 in my_dict.values())

# get fucntion

print(my_dict['Apple'])
print(my_dict.get('Apple'))


# print(my_dict['Apples'])
print(my_dict.get('Apples'))


# update function:

my_dict['Banana'] = 300

new_dict = {'Banana': 300, 'Apple': 200, 'Almond': 800, 'Nut': 190}

my_dict.update(new_dict)

print(my_dict)
my_dict['Apple'] = 500


print(my_dict)

print(new_dict)

# del

del my_dict['Almond']

print(my_dict)

# del my_dict

# print(my_dict)

# a = 10

# del a

# print(a)

# Last function: clear

my_dict.clear()

print(my_dict)
