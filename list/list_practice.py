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
    for curr in list:
        if (curr == num):
            count += 1
    return count

# AllIndex:


[1, 8, 3, 6, 3, 7, 2, 4, 3, 7, 8]

ans = [2, 5, 9]


def find_index(my_list, num):
    idx = 0
    ans = []

    while(idx < len(my_list)):
        if(my_list[idx] == num):
            ans.append(idx)
        idx += 1

    return ans

# Max: return maximum element of list


def my_max(my_list):
    print("I am max function")
    ans = my_list[0]

    for curr in my_list:
        if ans < curr:
            ans = curr
    return ans


# Min: return minimum element of list
def my_min(my_list):
    ans = my_list[0]
    for curr in my_list:
        if ans > curr:
            ans = curr
    return ans


# remove_all:

def remove_all(my_list, num):
    count = my_count(my_list, num)

    for i in range(count):
        my_list.remove(num)


my_list = take_list_input()
print(my_list)

print("The sum of list = ", my_sum(my_list))
print("The avg of list = ", my_avg(my_list))
print("The count of 10 in list = ", my_count(my_list, 10))
print("The max of list = ", my_max(my_list))
print("The min of list = ", my_min(my_list))
print("The indices of 13 in my_list = ", find_index(my_list, 13))
print(my_list)
remove_all(my_list, 13)
print(my_list)
