houses = [int(i) for i in input().split("@")]

current_jump = 0

while True:
    commands = input()
    if commands == "Love!":
        break

    jump_length = commands.split()[1]
    jump_length = int(jump_length)
    current_jump += jump_length

    if current_jump >= len(houses):
        current_jump = 0

    if houses[current_jump] == 0:
        print(f"Place {current_jump} already had Valentine's day.")
    else:
        houses[current_jump] -= 2
        if houses[current_jump] == 0:
            print(f"Place {current_jump} has Valentine's day.")

print(f"Cupid's last position was {current_jump}.")

is_successful = True
count = 0

for i in houses:
    if not i == 0:
        is_successful = False
        count += 1

if is_successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")
