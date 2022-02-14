# Dict:

# my_dict = {
#     True: False,
#     "NewKeY": "true",
#     "NewKey": False,
#     (1, 4): "Ten",
#     (1, 4): "tuple",
#     10: "ten",
#     10.0: "Ten in point"
# }

# print(10 == 10.0)

# a = [1, 2]
# b = [1, 2]

# print(a == b)

# print(my_dict)
# print(type(my_dict))


my_dict = {
    "Apple": 100,
    "Orange": 25,
    "Kiwi": 75
}

#  Access elements using key

print(my_dict["Apple"])
print(my_dict["Kiwi"])
# print(my_dict["Grapes"])

# Lists are mutable,
my_dict["Apple"] = 200

print(my_dict["Apple"])
print(my_dict)

# Adding new elements to list

my_dict["Grapes"] = 150

my_dict[10] = True

print(my_dict["Grapes"])
print(my_dict)

# How to iterate dict:

# dict.keys() - return list of keys
# dict.items() - return list of tuples of key,value


print(my_dict.keys())
print(type(my_dict.keys()))

print(my_dict.items())
print(type(my_dict.items()))

print("This is keys of dict")

for key in my_dict.keys():
    print(key, " : ", my_dict[key])

for kartik, adi in my_dict.items():
    print(kartik, " : ", adi)
