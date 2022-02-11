my_list = [1, 7, 3, 6, 8, 8]

my_tuple = (1, 7, 3, 6, 8, 8, "Pawan")

print(type(my_list))
print(type(my_tuple))

# Lists are mutable
my_list[0] = 100

# Tuples are immutable
# my_tuple[0] = 100

print(my_list)
print(my_tuple)

print(my_tuple[::-1])

for item in my_tuple:
    print(item)

idx = 0

while(idx < len(my_tuple)):
    print(my_tuple[idx])
    idx += 1
