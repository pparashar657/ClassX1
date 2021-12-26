n = int(input("Enter any number : "))

curr = 2

while(curr < n):
    is_prime = True
    for i in range(2, curr):
        if (curr % i == 0):
            is_prime = False
            break

    if (is_prime):
        print(curr, end=" ")

    curr += 1
