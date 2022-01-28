# Operation 1: Concatenation

# list1 = [2, 6, 1, 4, 5]

# list2 = [7, 8, 9]

# list3 = list1 + list2

# print(list3)

# list1 = [4, 1, 5]
#list2 = ['abc', 'def', 12]

#list = list1 + list2 + list1

#list[0] = 100

# print(list)
# print(list1)


# Operation 2: Repetition


'''
a = 2

a + a + a
a * 3 == a + a + a
'''

# list = [1, 2, 3]
# list * 2 == list + list
# print(list*2)

# list = ["Pawan"]

# list = (list + list * 2)

# # list = list - list

# print(list)


# Operation 3: Slicing

# list = [1, 2, 9, 8, 4, 7, 6]

# print(list[2:4])
# print(list[:])

# print(list[:4])
# print(list[3:])

# print(list[2:] + list[2:6] + list[:6])


# print(list[1:-3])

# list = [1, 5, 7, 8, 4, 3]

# print(list[::])
# print(list[::2])
# print(list[1:5:2])

# print(list[:4:3])

# print(list[::-1])

# print(list[2:5:-1])
# print(list[5:2:-1])

# print(list[5::-1])

# print(list[:2:-1])


# list = [1, 5, 7, 8, 4, 3]

# print(list[1:-1:1])

# print(list[-1:0:-1])

# print(list[-5:-1:-1])

# Operation 4: Includes


list = ["Apple", "orange", "Kiwi"]

if('Orange' not in list):
    print("My fruits has orange")
else:
    print("Fruits does not contain orange")
