max_marks = int(input('Enter max marks for each subject : '))

sub1 = int(input('Enter marks for subject 1 : '))
sub2 = int(input('Enter marks for subject 2 : '))
sub3 = int(input('Enter marks for subject 3 : '))

marks_obtained = sub1 + sub2 + sub3
total_marks = max_marks * 3

percentage = (marks_obtained/total_marks)*100

print('Percentage = ', percentage)
