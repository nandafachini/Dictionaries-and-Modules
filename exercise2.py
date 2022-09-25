# Fill a dictionary with the data of 5 students.
# Use the student's id as a key and a list of three grades as a value.
# Request data from the user.
# Scroll through the dictionary and display each student's average.

students = {}

for x in range (5):
    id = int(input("Insert you Student ID: "))
    grades = list(map(float, input("Insert your three grades without commas: ").split()))
    if len(grades) > 3:
        grades = grades[0], grades[1], grades[2] 
    students[id] = grades

a = 1
for x in students:
    student_average = sum(students.get(x))/3
    print(f'Average student grades with ID {x} = ' , student_average)
    a = a + 1
