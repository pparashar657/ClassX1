#n = int(input('How many fibonacci numbers you want to print ? '))

max = int(input('Enter the upper limit ? '))

first = 0
second = 1
third = 1

print(first, second, end=" ")

while(third < max):
    print(third, end=" ")
    third = first + second
    first = second
    second = third


'''
for i in range(2, n):
    third = first + second
    print(third, end=" ")
    first = second
    second = third

'''
