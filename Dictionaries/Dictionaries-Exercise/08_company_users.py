company_data = {}

while True:
    command = input()
    if command == "End":
        break

    [company, employee_id] = command.split(" -> ")
    if company not in company_data:
        company_data[company] = [employee_id]
    else:
        if employee_id not in company_data[company]:
            company_data[company] += [employee_id]

filtered_employee_id = sorted(company_data.items(), key=lambda x: x[0])

for company, employee_id in filtered_employee_id:
    print(f"{company}")
    for employee in employee_id:
        print(f"-- {employee}")
