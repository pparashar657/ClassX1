n = int(input("Enter any number : "))

count = 0
curr = 2

while(count < n):
    is_prime = True
    for i in range(2, curr):
        if (curr % i == 0):
            is_prime = False
            break

    if (is_prime):
        print(curr)
        count += 1

    curr += 1
