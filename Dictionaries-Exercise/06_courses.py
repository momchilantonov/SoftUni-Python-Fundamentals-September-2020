courses = {}

while True:
    command = input()
    if command == "end":
        break

    [course, name] = command.split(" : ")
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course] += [name]

ordered_courses = sorted(courses.items(), key=lambda x: -len(x[1]))

for course, names in ordered_courses:
    print(f"{course}: {len(courses[course])}")
    for name in sorted(names):
        print(f"-- {name}")
