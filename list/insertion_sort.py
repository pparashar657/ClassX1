
def insertion_sort(list):
    n = len(list)
    # Outer loop: to control number of iterations
    for i in range(n):
        # Inner loop: to insert element at its correct position.
        curr = list[i]
        pos = i-1
        while(pos >= 0 and list[pos] > curr):
            list[pos+1] = list[pos]
            pos -= 1
        list[pos+1] = curr


my_list = [10, 2, 3, 6, 2, 8, 1]

insertion_sort(my_list)

print(my_list)
