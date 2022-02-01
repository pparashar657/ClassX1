def take_list_input():
    n = int(input("How many numbers you want to enter? "))
    my_list = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1} : "))
        my_list.append(num)
    return my_list


my_list = take_list_input()
print(my_list)
