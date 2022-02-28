# Inbuilt modules

# Module 1: Math

# import math

# print(math.sqrt(25))

# # ceil function

# print(math.ceil(-1.5))

# print(math.floor(-1.5))

# # print(abs(10.56))
# # print(abs(-10.56))

# print(math.fabs(10.56))
# print(math.fabs(-10.56))

# # factorial

# print(math.factorial(4))

# # gcd

# print(math.gcd(10, 4))

# # LCM

# num1 = 10
# num2 = 15

# lcm = (num1 * num2)/(math.gcd(num1, num2))
# print(lcm)

# # pow
# print(pow(2, 6))
# print(2**6)
# print(math.pow(2, 6))


# Random module

# import random as rd

# # random

# print(rd.random())

# # randint

# print(rd.randint(1, 50))

# # randrange

# print(rd.randrange(10))

# Module statistics

import statistics as st

list = [1, 5, 2, 6, 8, 4, 65, 2, 4, 6, 78, 4, 23]

print(st.mean(list))
print(sum(list)/len(list))

print(st.mode(list))

print(st.median(list))
