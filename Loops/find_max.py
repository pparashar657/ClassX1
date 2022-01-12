n = int(input(" enter an number  = "))
max = 0
max2 = 0
for i in range(n):
    num = int(input())
    if (num > max):
        max2 = max
        max = num
    elif (num > max2):
        max2 = num


print("the max is ", max)
print("the max2=", max2)
