n1 = int(input("Enter num 1: "))
n2 = int(input("Enter num 2: "))
n3 = int(input("Enter num 3: "))

'''

if (n1 > n2 and n1 > n3):
    if (n2 > n3):
        print('The elements in sorted order are :', n1, n2, n3)
    else:
        print('The elements in sorted order are :', n1, n3, n2)


if (n2 > n1 and n2 > n3):
    if (n1 > n3):
        print('The elements in sorted order are :', n2, n1, n3)
    else:
        print('The elements in sorted order are :', n2, n3, n1)


if (n3 > n1 and n3 > n2):
    if (n1 > n2):
        print('The elements in sorted order are :', n3, n1, n2)
    else:
        print('The elements in sorted order are :', n3, n2, n1)


'''


if (n1 > n2 and n1 > n3):
    if (n2 > n3):
        print('The elements in sorted order are :', n1, n2, n3)
    else:
        print('The elements in sorted order are :', n1, n3, n2)

elif (n2 > n3):
    if (n1 > n3):
        print('The elements in sorted order are :', n2, n1, n3)
    else:
        print('The elements in sorted order are :', n2, n3, n1)

else:
    if (n1 > n2):
        print('The elements in sorted order are :', n3, n1, n2)
    else:
        print('The elements in sorted order are :', n3, n2, n1)
