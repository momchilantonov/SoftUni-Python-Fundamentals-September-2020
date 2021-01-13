rows_in_battle_field = int(input())
battle_field = []
counter = 0


def check_row(index, board):
    for i in range(len(board)):
        if index == i:
            return board[i]


for i in range(rows_in_battle_field):
    input_row = input().split(" ")
    data_row = [int(i) for i in input_row]
    battle_field.append(data_row)

attacks = input().split(" ")

for i in range(len(attacks)):
    row, col = attacks[i].split("-")
    attack_row = int(row)
    attack_col = int(col)
    row_for_check = check_row(attack_row, battle_field)
    for i in range(len(row_for_check)):
        if attack_col == i:
            if row_for_check[i] == 0:
                continue
            else:
                row_for_check[i] -= 1
                if row_for_check[i] == 0:
                    counter += 1

print(counter)
