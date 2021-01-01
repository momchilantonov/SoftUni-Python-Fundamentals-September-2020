from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_flour = 0

for student in range(students+1):
    if not student == 0 and student % 5 == 0:
        free_flour += 1

apron_sum = apron_price*(ceil(students*1.2))
egg_sum = egg_price*10*students
flour_sum = flour_price*(students-free_flour)
total_sum = apron_sum+egg_sum+flour_sum

if total_sum <= budget:
    print(f"Items purchased for {total_sum:.2f}$.")
else:
    needed_money = total_sum-budget
    print(f"{needed_money:.2f}$ more needed.")
