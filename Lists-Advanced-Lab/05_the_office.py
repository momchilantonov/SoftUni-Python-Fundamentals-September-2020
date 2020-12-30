employee_happiness = [int(coefficient) for coefficient in input().split()]
happiness_factor = int(input())

average_employee_happiness = sum([single_happiness * happiness_factor
                                  for single_happiness in employee_happiness]) / len(employee_happiness)

happy_employee_list = [single_happiness * happiness_factor
                       for single_happiness in employee_happiness
                       if single_happiness * happiness_factor >= average_employee_happiness]

if len(happy_employee_list) >= len(employee_happiness) / 2:
    print(f"Score: {len(happy_employee_list)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employee_list)}/{len(employee_happiness)}. Employees are not happy!")
