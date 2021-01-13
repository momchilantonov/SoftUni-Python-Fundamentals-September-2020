cards = input().split()
n_faro_shuffles = int(input())

half_deck = len(cards) // 2

for shuffle in range(n_faro_shuffles):
    left_deck = cards[1:half_deck]
    right_deck = cards[half_deck:len(cards)-1]
    shuffle_deck = []
    for card in range(len(left_deck)):
        shuffle_deck.append(right_deck[card])
        shuffle_deck.append(left_deck[card])

    cards[1:len(cards)-1] = shuffle_deck

print(cards)
