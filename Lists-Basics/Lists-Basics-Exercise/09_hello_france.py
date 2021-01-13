collection_of_items = input().split("|")
start_budget = float(input())

profit = 0
interim_budget = 0
profit_list = []

type_items = [index.split("->")[0] for index in collection_of_items]
price_items = [float(index.split("->")[1]) for index in collection_of_items]

for i in range(len(type_items)):
    sell_price = 0
    if type_items[i] == "Clothes" and price_items[i] > 50:
        continue
    elif type_items[i] == "Shoes" and price_items[i] > 35:
        continue
    elif type_items[i] == "Accessories" and price_items[i] > 20.5:
        continue

    if start_budget >= price_items[i]:
        sell_price += price_items[i] * 1.4
        profit += price_items[i] * 1.4-price_items[i]
        start_budget -= price_items[i]
        interim_budget += price_items[i] * 1.4
        profit_list.append(f"{sell_price:.2f}")

profit_list = " ".join(str(i) for i in profit_list)

print(profit_list)
print(f"Profit: {profit:.2f}")

total_budget = interim_budget+start_budget

if total_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
