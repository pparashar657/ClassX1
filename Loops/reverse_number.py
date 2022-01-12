def print_reverse(num):
    while(num > 0):
        digit = num % 10
        print(digit, end="")
        num //= 10


def reverse_number(num):
    ans = 0
    while(num > 0):
        digit = num % 10
        ans = ans * 10 + digit
        num //= 10
    return ans


num = int(input("Enter any number : "))

# print_reverse(num)
ans = reverse_number(num)
print("The reversed number = ", ans)
