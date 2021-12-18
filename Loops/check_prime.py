num = int(input('Enter any number : '))

is_prime = True

for i in range(2, num):
    if(num % i == 0):
        is_prime = False
        break

if is_prime:
    print('Yes my num is prime')
else:
    print('No my num is not prime')
