n = int(input('How many fibonacci numbers you want to print ? '))

first = 1
second = 1
#count = 2

print(first, second, end=" ")

'''
while(count < n):
    third = first + second
    print(third, end=" ")
    first = second
    second = third
    count += 1
print()
print(first, second, third)

'''


for i in range(2, n):
    third = first + second
    print(third, end=" ")
    first = second
    second = third
