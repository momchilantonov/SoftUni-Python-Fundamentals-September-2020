number_of_plants = int(input())
plants_data = {}

for _ in range(number_of_plants):
    [plant, rarity] = input().split("<->")
    rarity = int(rarity)
    if plant not in plants_data:
        plants_data[plant] = {"rarity": rarity, "rating": []}
    else:
        plants_data[plant]["rarity"] += rarity

while True:
    command = input()
    if command == "Exhibition":
        break

    actions = command.split(":")
    current_action = actions[0]
    current_data = actions[1].split(" - ")

    if current_action == "Rate":
        current_plant = current_data[0].strip()
        current_rating = int(current_data[1])
        if current_plant not in plants_data:
            print("error")
            continue
        plants_data[current_plant]["rating"].append(current_rating)
    elif current_action == "Update":
        current_plant = current_data[0].strip()
        new_rarity = int(current_data[1])
        if current_plant not in plants_data:
            print("error")
            continue
        plants_data[current_plant]["rarity"] = new_rarity
    elif current_action == "Reset":
        current_plant = current_data[0].strip()
        if current_plant not in plants_data:
            print("error")
            continue
        plants_data[current_plant]["rating"].clear()
    else:
        print("error")

for rating in plants_data.values():
    if len(rating["rating"]) > 0:
        rating["rating"] = (sum(rating["rating"]) / len(rating["rating"]))
    else:
        rating["rating"] = 0

filtered_plants = sorted(plants_data.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"]))

print("Plants for the exhibition:")

for plant, data in filtered_plants:
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {data['rating']:.2f}")
