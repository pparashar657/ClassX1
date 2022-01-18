def pattern4(n):
    for row in range(1, n+1):
        for col in range(1, n+1):
            if (col <= n - row):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()


n = int(input("Enter any number : "))

pattern4(n)
