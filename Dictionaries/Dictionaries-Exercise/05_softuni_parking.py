num = int(input())
register_users = {}

for i in range(num):
    data = input().split(" ")
    if len(data) == 3:
        type = data[0]
        name = data[1]
        plate = data[2]
    else:
        type = data[0]
        name = data[1]

    if type == "register":
        if name in register_users:
            print(f"ERROR: already registered with plate number {register_users[name]}")
        else:
            register_users[name] = plate
            print(f"{name} registered {plate} successfully")
    elif type == "unregister":
        if name not in register_users:
            print(f"ERROR: user {name} not found")
        else:
            register_users.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in register_users.items():
    print(f"{name} => {plate}")
