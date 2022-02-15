
n = int(input('How many employees? '))

my_dict = {}

for curr in range(1, n+1):
    name = input(f'Enter the name of employee {curr}: ')
    salary = int(input(f'Enter the salary of employee {curr}: '))
    my_dict[name] = salary

for name, salary in my_dict.items():
    print(f'The salary of {name} is {salary}')
