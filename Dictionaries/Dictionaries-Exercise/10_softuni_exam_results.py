exam_languages = {}
exam_results = {}

while True:
    command = input()
    if command == "exam finished":
        break

    exam_data = command.split("-")
    if len(exam_data) == 3:
        [user, language, points] = exam_data
        points = int(points)
        if user not in exam_results:
            exam_results[user] = points
        else:
            if exam_results[user] <= points:
                exam_results[user] = points
            else:
                exam_results[user] = exam_results[user]
        if language not in exam_languages:
            exam_languages[language] = 1
        else:
            exam_languages[language] += 1
    else:
        [user, _] = exam_data
        exam_results.pop(user)

print("Results:")

filtered_results = sorted(exam_results.items(), key=lambda x: (-x[1], x[0]))

for user, points in filtered_results:
    print(f"{user} | {points}")

print(f"Submissions:")

filtered_languages = sorted(exam_languages.items(), key=lambda x: (-x[1], x[0]))

for language, count in filtered_languages:
    print(f"{language} - {count}")
