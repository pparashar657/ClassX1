'''
print("1 = ", False and False)
print("2 = ", True and False)
print("3 = ", False or False)
print("4 = ", True or False)
print("5 = ", False and True)
print("6 = ", False or False)
print("7 = ", True or False)
print("8 = ", not True)
'''

a = 10
b = 20

print(a >= 10 and b <= 20)

print(not(a < b) or a == 10)

print(not(a <= 10 and not(20 >= b)) or (a > 20))
