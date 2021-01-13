dungeon_rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
room_counter = 0
is_alive = True

for room in dungeon_rooms:
    [command, value] = room.split(" ")
    value = int(value)
    room_counter += 1
    if command == "potion":
        needed_hp = 100-initial_health
        initial_health += value
        if initial_health > 100:
            print(f"You healed for {needed_hp} hp.")
            initial_health = 100
        else:
            print(f"You healed for {value} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        initial_health -= value
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            is_alive = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break

if room_counter == len(dungeon_rooms) and is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
