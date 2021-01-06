symbols_length = int(input())
symbol_list = [input() for i in range(symbols_length)]
bracket_list = [i for i in symbol_list if i == "(" or i == ")"]
open_list = bracket_list.count("(")
close_list = bracket_list.count(")")
its_open = False

for br in bracket_list:
    if br == "(" and not its_open:
        its_open = True
    elif br == "(" and its_open:
        break
    elif br == ")" and its_open:
        its_open = False
    elif br == ")" and not its_open:
        break

if open_list == close_list and not its_open:
    print("BALANCED")
else:
    print("UNBALANCED")
