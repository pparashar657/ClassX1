def pattern5(n):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if (col <= n - row):
                print(' ', end=" ")
            else:
                print((row + col - n), end=" ")
        print()


def pattern5_v2(n):
    for row in range(1, n + 1):
        # Print spaces
        for space_col in range(n-row):
            print(" ", end=' ')

        # Print Stars
        for val_col in range(1, row+1):
            print(val_col, end=" ")

        print()


n = int(input("Enter any number : "))

pattern5_v2(n)
