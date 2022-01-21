
def pattern1(n):
    for row in range(1, n+1):
        for col in range(1, row + 1):
            print("*", end=" ")
        print()


def pattern2(n):
    for row in range(1, n+1):
        for col in range(1, n - row + 2):
            print("*", end=" ")
        print()


def pattern6(n):
    for row in range(1, 2*n):
        if(row <= n):
            colNum = row
        else:
            colNum = 2*n - row

        for col in range(1, colNum + 1):
            print("*", end=" ")
        print()


def pattern6_v2(n):
    pattern1(n)
    pattern2(n-1)


def pattern7(n):
    for row in range(1, 2*n):
        if(row <= n):
            colNum = n + 1 - row
        else:
            colNum = row - n + 1
        for col in range(1, colNum + 1):
            print(row, end=" ")
        print()


def pattern7_v2(n):
    pattern2(n)
    pattern1(n)


n = int(input("Enter any number : "))

pattern7(n)
