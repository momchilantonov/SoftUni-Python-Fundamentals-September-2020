electrons_qty = int(input())

electrons_list = []
cell = 1

while electrons_qty > 0:
    possible_electrons = 2 * cell ** 2
    if electrons_qty < possible_electrons:
        electrons_list.append(electrons_qty)
    else:
        electrons_list.append(possible_electrons)
    cell += 1
    electrons_qty -= possible_electrons

print(electrons_list)
