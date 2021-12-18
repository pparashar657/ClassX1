num = int(input('Enter any number : '))

first = 0
second = 1
third = 1

while(third < num):
    third = first + second
    first = second
    second = third

if (third == num):
    print('Yes the number is fibonacci')
else:
    print('No the number is not fibonacci')
