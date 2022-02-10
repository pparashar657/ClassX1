def take_list_input():
    n = int(input("How many numbers you want to enter? "))
    my_list = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1} : "))
        my_list.append(num)
    return my_list


def reverse(my_list):
    i = 0
    j = len(my_list) - 1

    while(i < j):
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
        i += 1
        j -= 1


list = take_list_input()

print("Original list = ", list)

reverse(list)

print("Reversed list = ", list)
