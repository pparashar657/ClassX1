def pattern2(n):
    for row in range(1, n + 1):
        for col in range(1, row+1):
            print(n - col + 1, end=" ")
        print()


def pattern3(n):
    for row in range(1, n + 1):
        for col in range(1, row+1):
            print(n - row + 1, end=" ")
        print()


n = int(input("Enter any number : "))

# pattern2(n)
pattern3(n)
