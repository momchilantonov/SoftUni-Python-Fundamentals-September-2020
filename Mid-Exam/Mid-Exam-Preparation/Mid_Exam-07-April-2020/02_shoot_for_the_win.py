targets = [int(i) for i in input().split(" ")]

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index <= len(targets)-1 and not targets[index] == -1:
        for i in range(len(targets)):
            if not targets[i] == -1 and not i == index:
                if targets[i] > targets[index]:
                    targets[i] -= targets[index]
                elif targets[i] <= targets[index]:
                    targets[i] += targets[index]
        targets[index] = -1

print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(i) for i in targets)}")
