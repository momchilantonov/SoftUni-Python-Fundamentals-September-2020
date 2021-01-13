neighbors = [int(i) for i in input().split("@")]

current_index = 0

while True:
    command = input()
    if command == "Love!":
        break
    step = command.split()[1]
    step = int(step)
    current_index += step
    if current_index >= len(neighbors):
        current_index = 0
    if neighbors[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        neighbors[current_index] -= 2
        if neighbors[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {current_index}.")

is_success = True
count = 0

for i in neighbors:
    if not i == 0:
        is_success = False
        count += 1

if is_success:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")
