def take_list_input():
    n = int(input("How many numbers you want to enter? "))
    my_list = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1} : "))
        my_list.append(num)
    return my_list

# Sum


def my_sum(my_list):
    sum = 0
    for num in my_list:
        sum = sum + num
    return sum

# Avg:


def my_avg(list):
    return my_sum(list)/len(list)

# Count


def my_count(list, num):
    count = 0
    for i in list:
        if (i == num):
            count += 1
    return count

# AllIndex

# Max:

# Min:

# remove_all:


my_list = take_list_input()
print(my_list)

print("The sum of list = ", my_sum(my_list))
print("The avg of list = ", my_avg(my_list))
print("The count of 10 in list = ", my_count(my_list, 10))
