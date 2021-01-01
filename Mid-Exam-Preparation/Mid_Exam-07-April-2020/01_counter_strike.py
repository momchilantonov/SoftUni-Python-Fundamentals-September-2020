initial_energy = int(input())
battle_counter = 0
won_counter = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_counter}. Energy left: {initial_energy}")
        break
    distance = int(command)
    if initial_energy >= distance:
        initial_energy -= distance
        won_counter += 1
        battle_counter += 1
    else:
        print(f"Not enough energy! Game ends with {battle_counter} won battles and {initial_energy} energy")
        break
    if battle_counter % 3 == 0:
        initial_energy += battle_counter
