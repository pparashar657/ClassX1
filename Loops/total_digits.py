n = int(input("Enter any number : "))


def get_total_digit(num):
    total_digits = 0

    while(num > 0):
        total_digits += 1
        num //= 10

    return total_digits


ans = get_total_digit(n)

print(f'The total number of digits in {n} = {ans}')
