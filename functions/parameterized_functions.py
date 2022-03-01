
def my_function(num1, num2=10, num3=0):
    print("num1", num1)
    print("num2", num2)
    print("num3", num3)
    ans = num1 + num2 + num3
    return ans


# sum = my_function(1, 2, 3)
sum = my_function(1, 2, 3)
print(sum)

# Keyword arguments

sum2 = my_function(20, num3=10, num2=16)
