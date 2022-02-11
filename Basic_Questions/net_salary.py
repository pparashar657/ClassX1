basic = int(input("Enter your basic salary : "))

da = 0.15 * basic
hra = 0.25 * basic
ta = 0.07 * basic

pf = 0.12 * (basic + da + hra + ta)

agg_salary = (basic + da + hra + ta) - pf

if (agg_salary <= 5000):
    grade = 'C'
elif (agg_salary <= 7000):
    grade = 'B'
else:
    grade = 'A'

if (grade == 'A'):
    bonus = 5000
elif (grade == 'B'):
    bonus = 3000
elif (grade == 'C'):
    bonus = 1000
else:
    bonus = 0

net_salary = agg_salary + bonus

print(f'The net salary for basic = {basic} is : {net_salary}')
