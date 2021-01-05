num_of_pieces = int(input())
pieces_data = {}

for pieces in range(num_of_pieces):
    [piece, composer, key] = input().split("|")
    pieces_data[piece] = {"composer": composer, "key": key}


def add(data, piece, composer, key):
    if piece not in data:
        data[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
        return data
    else:
        print(f"{piece} is already in the collection!")
        return data


def remove(data, piece):
    if piece not in data:
        print(f"Invalid operation! {piece} does not exist in the collection.")
        return data
    else:
        del data[piece]
        print(f"Successfully removed {piece}!")
        return data


def change(data, piece, key):
    if piece not in data:
        print(f"Invalid operation! {piece} does not exist in the collection.")
        return data
    else:
        data[piece]["key"] = key
        print(f"Changed the key of {piece} to {key}!")
        return data


while True:
    command = input()
    if command == "Stop":
        break

    actions = command.split("|")
    action = actions[0]
    if action == "Add":
        curr_piece = actions[1]
        curr_composer = actions[2]
        curr_key = actions[3]
        pieces_data = add(pieces_data, curr_piece, curr_composer, curr_key)
    elif action == "Remove":
        curr_piece = actions[1]
        pieces_data = remove(pieces_data, curr_piece)
    elif action == "ChangeKey":
        curr_piece = actions[1]
        new_key = actions[2]
        pieces_data = change(pieces_data, curr_piece, new_key)

filtered_pieces = sorted(pieces_data.items(), key=lambda x: (x[0], x[1]["composer"]))

for piece, data in filtered_pieces:
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")
