def pattern4(n):
    for row in range(1, n+1):
        for col in range(1, n+1):
            if (col <= n - row):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()


def pattern4_v2(n):
    for row in range(1, n + 1):
        # Print spaces
        for col in range(n-row):
            print(" ", end=' ')

        # Print Stars
        for col in range(row):
            print("*", end=" ")

        print()


n = int(input("Enter any number : "))

pattern4_v2(n)
