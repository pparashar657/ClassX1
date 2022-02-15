def doubleValue(my_dict):
    for key in my_dict.keys():
        my_dict[key] = my_dict[key] * 2
    print("I am inside func and dict = ", my_dict)


my_dict = {
    "Apple": 100,
    "Orange": 25,
    "Kiwi": 75
}

new_dict = my_dict

my_dict['Mango'] = 190

print(my_dict)
print(new_dict)

doubleValue(my_dict)

print("I am outside func and dict = ", my_dict)
