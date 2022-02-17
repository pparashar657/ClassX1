
# from re import A


# Pawan A
# Adi B
# Kartik B
# Chirag C
# Pankaj A
# Boss D

# The students of HOuse A:
# Pawan
# Pankaj

# The students of House B:
# Adi
# Kartik

n = int(input('enter the no of student :', ))
student_data = {}
for i in range(n):
    student_name = input(f'enter the student name {i+1} :')
    student_house = input(f'enter the student house {i+1} :')

    if student_house in student_data:
        student_data[student_house].append(student_name)
    else:
        student_data[student_house] = [student_name]

print("Student Data:")
print(student_data)

print("House wise details: ")

for house, names_list in student_data.items():
    print(f"The students of House {house} are :")
    for name in names_list:
        print(name)
