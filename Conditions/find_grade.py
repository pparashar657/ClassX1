marks = int(input("Enter the marks out of 100 : "))

grade = None

'''

if (marks >= 90):
    grade = 'A'

if (marks >= 80 and marks < 90):
    grade = 'B'

if (marks >= 70 and marks < 80):
    grade = 'C'

if (marks < 70):
    grade = 'F'


'''
'''
if (marks >= 90):
    grade = 'A'
else:
    if (marks >= 80):
        grade = 'B'
    else:
        if (marks >= 70):
            grade = 'C'
        else:
            grade = 'F'

'''

if (marks >= 90):
    grade = 'A'
elif (marks >= 80):
    grade = 'B'
elif (marks >= 70):
    grade = 'C'
else:
    grade = 'F'

print(f'The grade for {marks} marks =', grade)
