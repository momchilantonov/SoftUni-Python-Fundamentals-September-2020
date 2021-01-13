employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
people_count = int(input())

time_for_responds = 0

responds_per_hour = employee_1+employee_2+employee_3

while people_count > 0:
    people_count -= responds_per_hour
    time_for_responds += 1
    if time_for_responds % 4 == 0:
        time_for_responds += 1

print(f"Time needed: {time_for_responds}h.")
