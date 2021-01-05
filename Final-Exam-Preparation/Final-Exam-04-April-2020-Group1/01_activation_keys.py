activation_key = input()


def is_contains(a_key, substring):
    if substring in a_key:
        return f"{a_key} contains {substring}"
    return "Substring not found!"


def flip_part(a_key, action, index_1, index_2):
    index_1 = int(index_1)
    index_2 = int(index_2)
    part_for_flip = a_key[index_1:index_2]
    if action == "Upper":
        a_key = a_key.replace(part_for_flip, part_for_flip.upper(), 1)
        print(a_key)
        return a_key
    elif action == "Lower":
        a_key = a_key.replace(part_for_flip, part_for_flip.lower(), 1)
        print(a_key)
        return a_key


def slice_part(a_key, index_1, index_2):
    index_1 = int(index_1)
    index_2 = int(index_2)
    part_for_slice = a_key[index_1:index_2]
    a_key = a_key.replace(part_for_slice, "", 1)
    print(a_key)
    return a_key


while True:
    command = input()
    if command == "Generate":
        break

    instruction = command.split(">>>")

    if instruction[0] == "Contains":
        print(is_contains(activation_key, instruction[1]))
    elif instruction[0] == "Flip":
        activation_key = flip_part(activation_key, instruction[1], instruction[2], instruction[3])
    elif instruction[0] == "Slice":
        activation_key = slice_part(activation_key, instruction[1], instruction[2])

print(f"Your activation key is: {activation_key}")
