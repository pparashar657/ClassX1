num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))

max = None

'''
if (num1 > num2 and num1 > num3):
    max = num1
if (num2 > num1 and num2 > num3):
    max = num2
if (num3 > num1 and num3 > num2):
    max = num3

'''

if (num1 > num2 and num1 > num3):
    max = num1
elif (num2 > num3):
    max = num2
else:
    max = num3

print(f'The maximum of {num1}, {num2} and {num3} is {max}')
