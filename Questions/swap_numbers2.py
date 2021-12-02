num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

print("Before swapping : ")
print('num1 = ', num1)
print('num2 = ', num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping : ")
print('num1 = ', num1)
print('num2 = ', num2)
