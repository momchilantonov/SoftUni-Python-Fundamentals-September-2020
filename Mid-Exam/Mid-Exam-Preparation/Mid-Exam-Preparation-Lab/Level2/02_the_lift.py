people = int(input())
lift_state = [int(el) for el in input().split(" ")]

for i in range(len(lift_state)):
    while not lift_state[i] == 4:
        if people > 0:
            lift_state[i] += 1
            people -= 1
        else:
            break

if people <= 0 and sum(lift_state) < len(lift_state) * 4:
    print("The lift has empty spots!")
elif people > 0 and sum(lift_state) == len(lift_state) * 4:
    print(f"There isn't enough space! {people} people in a queue!")

lift_state = [str(el) for el in lift_state]
print(f"{' '.join(lift_state)}")
