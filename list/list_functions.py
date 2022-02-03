
# my_list = [1, 5, 2, 6, 7, 3, 9]

# # len: returns length of input

# print(len(my_list))

# # sum: returns sum of input

# print(sum(my_list))

# # Average:

# print(sum(my_list) / len(my_list))

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

# my_list = [1, 3, 9]

# # append: adds element to last

# print(my_list)

# my_list.append(10)
# my_list.append(11)

# print(my_list)


# # extend fucntion: concat two lists

# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]

# my_list1.extend(my_list2)
# my_list2.extend(my_list1)

# # my_list1 += my_list2
# # my_list2 += my_list1

# print(my_list1)
# print(my_list2)


# # insert: add element ot a particluar index

# print(my_list)

# my_list.insert(2, "Pawan")
# my_list.append(10)
# print(my_list)
# my_list.insert(-1, 100)

# print(my_list)


my_list = [1, 7, 3, 8, 9, 3]

# Count: Count frequency of a number

# print(my_list.count(1))
# print(my_list.count(3))
# print(my_list.count(17))

# # index: returns index of an element

# print(my_list.index(7))

# print(my_list.index(3))

# This will give error
# print(my_list.index(13))

# # Remove : removes an item from list, only the first occurence | return None

# print(my_list)
# my_list.remove(7)
# print(my_list)
# my_list.remove(3)
# print(my_list)

# my_list.remove(13)

# print(my_list)

# # pop: removes the element corresponding to the given index
# idx = 2
# my_list.remove(my_list[idx])

# my_list.pop(2)

# print(my_list)

# Reverse function:
# my_list = [1, 7, 3, 8, 9, 3]

# print(my_list[::-1])

# my_list = my_list[::-1]

# print(my_list)

# my_list.reverse()

# print(my_list)

# # sort: re arrange the list in ascending order: ;Change the original list

# my_list.sort()

# print(my_list)
