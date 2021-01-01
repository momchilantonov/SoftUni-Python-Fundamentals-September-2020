num_students = int(input())
students_data = {}
average_grade_data = {}

for _ in range(num_students):
    student = input()
    grade = float(input())
    if student not in students_data:
        students_data[student] = [grade]
    else:
        students_data[student].append(grade)

for student, grade in students_data.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        average_grade_data[student] = average_grade

filtered_students = sorted(average_grade_data.items(), key=lambda x: -x[1])

for student, grade in filtered_students:
    print(f"{student} -> {grade:.2f}")



