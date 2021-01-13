tickets = input().split(", ")
winning_symbols = ["@", "$", "#", "^"]


def is_jackpot(checked_ticket):
    left_side = checked_ticket[0:10]
    right_side = checked_ticket[10:20]
    if not left_side == right_side:
        return False
    for winning_symbol in winning_symbols:
        if winning_symbol * 10 == left_side:
            print(f'ticket "{checked_ticket}" - 10{winning_symbol} Jackpot!')
            return True
    return False


def is_winning(checked_ticket):
    left_side = checked_ticket[0:10]
    right_side = checked_ticket[10:20]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_side and winning_symbol * 6 in right_side:
            count_left = left_side.count(winning_symbol)
            count_right = right_side.count(winning_symbol)
            count = min(count_left, count_right)
            print(f'ticket "{checked_ticket}" - {count}{winning_symbol}')
            return True
    return False


for t in tickets:
    ticket = t.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    if is_jackpot(ticket):
        continue

    if is_winning(ticket):
        continue

    print(f'ticket "{ticket}" - no match')
