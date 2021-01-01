parts = input().split("|")

while True:
    commands = input()
    if commands == "Done":
        break

    data_commands = commands.split(" ")

    if data_commands[1] == "Left":
        index = int(data_commands[2])
        if index <= len(parts)+1:
            new_index = index-1
            if index > 0:
                parts.insert(new_index, parts.pop(index))
    elif data_commands[1] == "Right":
        index = int(data_commands[2])
        if index <= len(parts)+1:
            new_index = index+1
            if new_index <= len(parts):
                parts.insert(new_index, parts.pop(index))
    elif data_commands[1] == "Odd":
        odds = [parts[i] for i in range(len(parts)) if i % 2 == 1]
        print(f"{' '.join(odds)}")
    elif data_commands[1] == "Even":
        evens = [parts[i] for i in range(len(parts)) if i % 2 == 0]
        print(f"{' '.join(evens)}")

print(f"You crafted {''.join(parts)}!")
