events = input().split("|")

energy = 100
coins = 100
is_managed = True

event_type = [i.split("-")[0] for i in events]
event_points = [int(i.split("-")[1]) for i in events]

for i in range(len(event_type)):
    if event_type[i] == "rest":
        if energy == 100:
            print(f"You gained 0 energy.")
            print(f"Current energy: 100.")
        elif energy + event_points[i] > 100:
            print(f"You gained {event_points[i]} energy.")
            print(f"Current energy: 100.")
        else:
            energy += event_points[i]
            print(f"You gained {event_points[i]} energy.")
            print(f"Current energy: {energy}.")
    elif event_type[i] == "order":
        if energy >= 30:
            energy -= 30
            coins += event_points[i]
            print(f"You earned {event_points[i]} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - event_points[i] > 0:
            coins -= event_points[i]
            print(f"You bought {event_type[i]}.")
        else:
            is_managed = False
            print(f"Closed! Cannot afford {event_type[i]}.")
            break

if is_managed and coins > 0 and energy > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
