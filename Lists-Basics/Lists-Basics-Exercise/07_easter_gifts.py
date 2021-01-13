gifts_names = input().split()

while True:
    command = input()
    if "No Money" in command:
        break
    elif "OutOfStock" in command:
        command_list = command.split()
        gifts_names = ["None" if gifts_names[i] == command_list[1] else gifts_names[i]
                       for i in range(len(gifts_names))]
    elif "Required" in command:
        command_list = command.split()
        gifts_names = [command_list[1] if i == int(command_list[2]) else gifts_names[i]
                       for i in range(len(gifts_names))]
    elif "JustInCase" in command:
        command_list = command.split()
        gifts_names = [command_list[1] if gifts_names[i] == gifts_names[-1] else gifts_names[i]
                       for i in range(len(gifts_names))]

gifts_names = [gifts_names[i] for i in range(len(gifts_names)) if not gifts_names[i] == "None"]
gifts_names = ' '.join([str(i) for i in gifts_names])

print(gifts_names)
