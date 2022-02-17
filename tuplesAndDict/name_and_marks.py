
n = int(input("How many students data you want to enter? "))

student_data = []

for i in range(n):
    name = input(f"Enter the name of student {i+1} : ")
    marks = int(input(f"Enter the marks of student {i+1} : "))

    student_data.append((name, marks))

print("Student Details:")
print(student_data)

print("Students with marks > 75% : ")

for name, marks in student_data:
    if (marks > 75):
        print(name)


# n = int(input("How many students data you want to enter? "))

# student_data = {}

# for i in range(n):
#     name = input(f"Enter the name of student {i+1} : ")
#     marks = int(input(f"Enter the marks of student {i+1} : "))

#     student_data[name] = marks

# print("Student Details:")
# print(student_data)

# print("Students with marks > 75% : ")

# for name, marks in student_data.items():
#     if (marks > 75):
#         print(name)
