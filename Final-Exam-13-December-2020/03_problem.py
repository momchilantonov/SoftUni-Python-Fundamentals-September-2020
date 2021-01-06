capacity = int(input())
username_data = {}


def add(data, user, s, r):
    if user not in data:
        data[user] = {"sent": s, "received": r}
        return data
    else:
        return data


def message(data, s, r, cap):
    if s in data and r in data:
        data[s]["sent"] += 1
        data[r]["received"] += 1
        if data[s]["sent"]+data[s]["received"] == cap:
            print(f"{s} reached the capacity!")
            del data[s]
        if data[r]["sent"]+data[r]["received"] == cap:
            print(f"{r} reached the capacity!")
            del data[r]
        return data
    else:
        return data


def empty(data, user):
    if user == "All":
        data.clear()
    if user in data:
        del data[user]
    return data


while True:
    command = input()
    if command == "Statistics":
        break

    actions = command.split("=")
    action = actions[0]

    if action == "Add":
        username = actions[1]
        sent = int(actions[2])
        received = int(actions[3])
        username_data = add(username_data, username, sent, received)
    elif action == "Message":
        sender = actions[1]
        receiver = actions[2]
        username_data = message(username_data, sender, receiver, capacity)
    elif action == "Empty":
        username = actions[1]
        username_data = empty(username_data, username)

count_users = len(username_data.keys())
print(f"Users count: {count_users}")

filtered_users = sorted(username_data.items(), key=lambda x: (-x[1]['received'], x[0]))

for key, val in filtered_users:
    print(f"{key} - {val['sent']+val['received']}")
