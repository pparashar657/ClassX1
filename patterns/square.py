def print_square_pattern(n):
    for row in range(n):
        for col in range(n):
            print(n, end=" ")
        print()


def print_square_pattern2(n):
    for row in range(n):
        for col in range(n):
            print(col+1, end=" ")
        print()


n = int(input("Enter any number : "))

print_square_pattern2(n)
