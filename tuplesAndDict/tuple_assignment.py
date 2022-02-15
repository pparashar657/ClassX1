
a = (10, 20)

print(a)
print(type(a))

x, y = (10, "Pawan")

print(x)
print(y)
print(type(x))
print(type(y))


# def findSumAndMax(my_list):

#     my_max = max(my_list)
#     my_sum = sum(my_list)

#     return my_sum, my_max


# list = [1, 6, 3, 4, 6, 3, 4]

# sum, max = findSumAndMax(list)
# print(sum)
# print(max)
# print(type(sum))
# print(type(max))

list = [1, 7, 3, 5, 2, 4, 7]

for curr in list:
    print(curr)

for idx, val in enumerate(list):
    print(idx, " : ", val)
