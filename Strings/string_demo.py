a = 'xjnasklcndac'
"nadfklvml;sm c,.   qw  xl21` \n \n \t \t"

b = """
This is
a multiline
string.
"""

print(a)
print(b)

'''
This is
a multiline
string.

'''

# Operations on string

a = "Pawan"
b = " Kumar"

c = a + b

d = c * 2

print(c)
print(d)

a = "Pawan"

b = a

b = b + " kumar"

print(a)
print(b)

print(a[0])

print(type(a[0]))

print(a[2:4])

print(a[::-1])

print(a[-2])

# Strings are immutable

# a[0] = 'k'

print(a)

a = "kartik"

b = "kartik"

print(a == b)

a = "Pawan is a good boy"

print("a" in a)


#  String traversal

str = "Pawan is a good boy"

for ch in str:
    print(ch)

idx = 0
while(idx < len(str)):
    print(str[idx])
    idx += 1
