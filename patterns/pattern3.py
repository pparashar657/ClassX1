def pattern3(n):
    for row in range(1, n+1):
        for col in range(1, n - row + 2):
            print("*", end=" ")
        print()


n = int(input("Enter any number : "))

pattern3(n)
