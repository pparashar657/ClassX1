
my_list = [1, 5, 2, 6, 7, 3, 9]

# len: returns length of input

print(len(my_list))

# sum: returns sum of input

print(sum(my_list))

# Average:

print(sum(my_list) / len(my_list))

# Empty list
# my_list = []
# my_list = list()

# my_list = list((1, 2, 3, 4, 5))

# Casting tuple to list

# print(type((1, 2, 3)))
# print(type(list((1, 2, 3))))

# print(len(my_list))


# ---------------------------------- #
# List Functions:

my_list = [1, 3, 9]

# append: adds element to last

print(my_list)

my_list.append(10)
my_list.append(11)

print(my_list)


# extend fucntion: concat two lists

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# my_list1.extend(my_list2)
# my_list2.extend(my_list1)

my_list1 += my_list2
my_list2 += my_list1

print(my_list1)
print(my_list2)


# insert: add element ot a particluar index

print(my_list)

my_list.insert(2, "Pawan")
my_list.append(10)
print(my_list)
my_list.insert(-1, 100)

print(my_list)
