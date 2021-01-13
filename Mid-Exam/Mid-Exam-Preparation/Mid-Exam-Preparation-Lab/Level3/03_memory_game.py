elements = [i for i in input().split()]

moves = 0

while True:
    command = input()
    if command == "end":
        break

    [el_1, el_2] = command.split()
    el_1 = int(el_1)
    el_2 = int(el_2)
    moves += 1
    if el_1 == el_2 or el_1 not in range(len(elements)) or el_2 not in range(len(elements)):
        elements.insert(int(len(elements) // 2), f"-{moves}a")
        elements.insert(int(len(elements) // 2+1), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    if elements[el_1] == elements[el_2]:
        print(f"Congrats! You have found matching elements - {elements[el_1]}!")
        elements = [el for el in elements if not el == elements[el_1] or not el == elements[el_2]]
    else:
        print("Try again!")
    if not elements:
        print(f"You have won in {moves} turns!")
        break

if len(elements) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(elements)}")
