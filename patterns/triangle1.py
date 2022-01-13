def print_right_triangle(n):
    for row in range(n):
        for col in range(row + 1):
            print("*", end=" ")
        print()


n = int(input("Enter any number : "))

print_right_triangle(n)
