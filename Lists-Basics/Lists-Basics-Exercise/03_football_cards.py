cards = input()

team_a = list()
team_b = list()

for i in range(1, 12):
    team_a.append(str(i))
    team_b.append(str(i))

list_cards = cards.split()
new_list_cards = []

for i in range(len(list_cards)):
    new_list_cards = list_cards[i].split('-')
    if new_list_cards[0] == "A":
        if new_list_cards[1] in team_a:
            team_a.remove(new_list_cards[1])
    elif new_list_cards[0] == "B":
        if new_list_cards[1] in team_b:
            team_b.remove(new_list_cards[1])
    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break

if len(team_a) >= 7 and len(team_b) >= 7:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
