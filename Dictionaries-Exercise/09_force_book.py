def add_user(forces_dict, side_to_join, user_to_add):
    for side, users in forces_dict.items():
        if user_to_add in users:
            return forces_dict
    if side_to_join not in forces_dict:
        forces_dict[side_to_join] = []
        forces_dict[side_to_join].append(user_to_add)
    else:
        if user_to_add not in forces_dict[side_to_join]:
            forces_dict[side_to_join].append(user_to_add)
    return forces_dict


def transfer_user(forces_dict, side_to_transfer, user_to_transfer):
    for side, users in forces_dict.items():
        if user_to_transfer in users:
            forces_dict[side].remove(user_to_transfer)
            return add_user(forces_dict, side_to_transfer, user_to_transfer)
    return add_user(forces_dict, side_to_transfer, user_to_transfer)


data = input()

forces = {}

while not data == "Lumpawaroo":
    data_list = data.split(' | ')

    if len(data_list) > 1:
        side, user = data.split(' | ')
        forces = add_user(forces, side, user)
    else:
        user, side = data.split(' -> ')
        forces = transfer_user(forces, side, user)
        print(f"{user} joins the {side} side!")
    data = input()


ordered_forces = sorted(forces.items(), key=lambda x: (-len(x[1]), x[0]))

for side, users in ordered_forces:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
