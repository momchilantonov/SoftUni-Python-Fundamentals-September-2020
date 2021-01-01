shopping_list = input().split("!")

while True:
    commands = input()
    if commands == "Go Shopping!":
        break
    command = commands.split()
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        for i in range(len(shopping_list)):
            if shopping_list[i] == command[1]:
                shopping_list[i] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])

print(f"{', '.join(shopping_list)}")
