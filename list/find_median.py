
def take_list_input():
    n = int(input("How many numbers you want to enter? "))
    my_list = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1} : "))
        my_list.append(num)
    return my_list


def find_median(list):
    sorted_list = sorted(list)
    my_len = len(sorted_list)
    if(my_len % 2 == 0):
        mid_index = my_len//2
        ans = (sorted_list[mid_index] + sorted_list[mid_index-1])/2
    else:
        ans = sorted_list[my_len//2]
    return ans


list = take_list_input()

median = find_median(list)

print("My median = ", median)
