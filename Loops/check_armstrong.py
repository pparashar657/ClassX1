def get_total_digit(num):
    total_digits = 0

    while(num > 0):
        total_digits += 1
        num //= 10

    return total_digits


def check_armstrong(num):
    total_digits = get_total_digit(num)
    temp = num
    sum = 0

    while(temp > 0):
        digit = temp % 10
        sum += (digit**total_digits)
        temp //= 10

    if (sum == num):
        return True
    else:
        return False


# ==================================
# Check given number is armstrong or not

num = int(input("enter the number : "))

# check_armstrong(num)

if(check_armstrong(num)):
    print("Yes the number is armstrong")
else:
    print("No the number is not armstrong")

# ==================================
# Print first n Armstrong numbers

n = int(input("How many numbers? "))

count = 0
curr = 1

while(count < n):
    if(check_armstrong(curr)):
        print(curr, end=" ")
        count += 1
    curr += 1

# ===================================
# Print Armstrong numbers upto a given number

num = int(input("Upto which number ? "))
curr = 1

while(curr < num):
    if(check_armstrong(curr)):
        print(curr, end=" ")
    curr += 1
