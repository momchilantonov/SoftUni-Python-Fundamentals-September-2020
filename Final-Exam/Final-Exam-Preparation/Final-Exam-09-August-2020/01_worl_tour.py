destinations = input()
initial_destinations = destinations

while True:
    command = input()
    if command == "Travel":
        break

    action = command.split(":")

    if action[0] == "Add Stop":
        index = int(action[1])
        changed_string = action[2]
        if 0 <= index < len(destinations):
            destinations = destinations[:index]+changed_string+destinations[index:]
        print(destinations)
    elif action[0] == "Remove Stop":
        index_1 = int(action[1])
        index_2 = int(action[2])
        if 0 <= index_1 < len(destinations) and 0 <= index_2 < len(destinations):
            destinations = destinations.replace(destinations[index_1: index_2+1], "", 1)
        print(destinations)
    elif action[0] == "Switch":
        old_string = action[1]
        new_string = action[2]
        if old_string in initial_destinations:
            destinations = destinations.replace(old_string, new_string)
        print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
