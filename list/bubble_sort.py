
def bubble_sort(list):
    n = len(list)
    # Loop for number of iterations
    for i in range(n):
        # Loop for each iteration.
        for curIdx in range(n-i-1):
            if(list[curIdx] > list[curIdx + 1]):
                (list[curIdx], list[curIdx+1]) = (list[curIdx+1], list[curIdx])


my_list = [10, 2, 3, 6, 2, 8, 1]

bubble_sort(my_list)

print(my_list)
