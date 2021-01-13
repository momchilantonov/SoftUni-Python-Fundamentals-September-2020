def shoot(n, i, v):
    if 0 <= i < len(n):
        n[i] -= v
        if n[i] <= 0:
            n.pop(i)
    return n


def add(n, i, v):
    if 0 <= i < len(n):
        n.insert(i, v)
    else:
        print("Invalid placement!")
    return n


def strike(n, i, v):
    left_i = i-v
    right_i = i+v
    if left_i >= 0 and right_i < len(n):
        left_part = n[:left_i]
        right_part = n[right_i+1:]
        n = left_part+right_part
    else:
        print("Strike missed!")
    return n


targets = [int(i) for i in input().split()]

while True:
    commands = input()
    if commands == "End":
        break
    action, index, value = commands.split()
    index = int(index)
    value = int(value)
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)

print("|".join(str(i) for i in targets))
