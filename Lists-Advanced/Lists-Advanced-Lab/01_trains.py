wagons_qty = int(input())

wagons = [0 for i in range(wagons_qty)]

command = input()

while not command == "End":
    commands_data = command.split()
    if commands_data[0] == "add":
        wagons[-1] += int(commands_data[1])
    elif commands_data[0] == "insert":
        wagons[int(commands_data[1])] += int(commands_data[2])
    elif commands_data[0] == "leave":
        wagons[int(commands_data[1])] -= int(commands_data[2])

    command = input()

print(wagons)
