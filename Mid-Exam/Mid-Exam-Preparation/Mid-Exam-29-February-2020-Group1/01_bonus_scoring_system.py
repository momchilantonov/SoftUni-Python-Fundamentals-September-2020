count_of_students = int(input())
count_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0

for student in range(count_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / count_of_lectures * (5+additional_bonus)
    if max_bonus < total_bonus:
        max_bonus = total_bonus
        max_attendance = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
