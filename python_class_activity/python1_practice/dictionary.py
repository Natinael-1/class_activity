student_grades = {"Abebe": 95, "Mulugeta": 89, "Meaza": 90}
for student, grade in student_grades.items():
    print(student, grade)
new_student = input("Please enter the name of the new student to add: ")
new_grade = input("What is the grade for the student?: ")
student_grades["new_student"] = "new_grade"
for stu, gra in student_grades.items():
    print(f"{stu} : {gra}")