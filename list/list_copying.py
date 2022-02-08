
# my_list = [1, 4, 2, 5, 6, 8, 4]

# num = 10

# new_list = my_list

# print(my_list)
# print(new_list)

# new_num = num

# print(num)
# print(new_num)


# -----------

# new_num = 20

# print(num)
# print(new_num)

# ------------

# num = 10


# def increase(num):
#     num += 1
#     print("I am inside func and num = ", num)
#     return num


# num = increase(num)

# print("My num = ", num)

# ---------------

my_list = [1, 5, 2, 6, 7, 8]

# new_list = my_list

# print(my_list)
# print(new_list)

# new_list[0] = 109

# print(my_list)
# print(new_list)


# def increase(func_list):
#     idx = 0
#     while(idx < len(func_list)):
#         func_list[idx] += 1
#         idx += 1
#     print("I am inside func, my_list = ", func_list)


# increase(my_list)

# print("I am outside func, my_list = ", my_list)

# ----------------------------
# Methods for copying list by value

# Method 1, copy all data by loop

# my_list = [1, 5, 2, 6, 8]
# new_list = []

# for val in my_list:
#     new_list.append(val)

# print(new_list)
# print(my_list)

# my_list[0] = 100

# print(new_list)
# print(my_list)


# Method 2: Copy by slicing

# my_list = [1, 5, 2, 6, 8]
# new_list = my_list[:]

# print(new_list)
# print(my_list)

# my_list[0] = 100

# print(new_list)
# print(my_list)

# Method 3: Use list()

# my_list = [1, 5, 2, 6, 8]
# new_list = list(my_list)

# print(new_list)
# print(my_list)

# my_list[0] = 100

# print(new_list)
# print(my_list)

my_list = [1, 7, [9, 8, 3, [5, 9, 12, 90]], True]

print(my_list[2][3][0])

print(my_list)

# idx = 0
# while(idx < len(my_list)):
#     print(my_list[idx])
#     print(type(my_list[idx]))
#     idx += 1

print(my_list[2][0])
print(my_list[2][2])

my_list[2].append(100)

print(my_list)
