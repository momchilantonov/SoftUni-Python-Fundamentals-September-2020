cities_data = {}


def is_city_visited(visited_towns, town, people, treasury):
    if town not in visited_towns:
        visited_towns[town] = [people, treasury]
    else:
        visited_towns[town][0] += people
        visited_towns[town][1] += treasury
    return visited_towns


def plunder_action(towns, robbed_town, killed_people, robbed_treasury):
    towns[robbed_town][0] -= killed_people
    towns[robbed_town][1] -= robbed_treasury
    print(f"{robbed_town} plundered! {robbed_treasury} gold stolen, {killed_people} citizens killed.")
    if towns[robbed_town][0] == 0 or towns[robbed_town][1] == 0:
        towns.pop(robbed_town)
        print(f"{robbed_town} has been wiped off the map!")
    return towns


def prosper_action(towns, growth_city, increasing_treasury):
    if increasing_treasury < 0:
        print("Gold added cannot be a negative number!")
        return towns
    towns[growth_city][1] += increasing_treasury
    print(f"{increasing_treasury} gold added to the city treasury. {growth_city} now has {towns[growth_city][1]} gold.")
    return towns


while True:
    targets = input()
    if targets == "Sail":
        break

    [city, population, gold] = targets.split("||")
    population = int(population)
    gold = int(gold)

    cities_data = is_city_visited(cities_data, city, population, gold)

while True:
    actions_data = input()
    if actions_data == "End":
        break

    action = actions_data.split("=>")

    if action[0] == "Plunder":
        robbed_city = action[1]
        killed_population = int(action[2])
        robbed_gold = int(action[3])
        cities_data = plunder_action(cities_data, robbed_city, killed_population, robbed_gold)
    elif action[0] == "Prosper":
        economic_growth_city = action[1]
        increasing_gold = int(action[2])
        cities_data = prosper_action(cities_data, economic_growth_city, increasing_gold)

filtered_settlements = sorted(cities_data.items(), key=lambda x: (-x[1][1], x[0][0]))

if len(cities_data) > 0:
    print(f"Ahoy, Captain! There are {len(cities_data)} wealthy settlements to go to:")
    for left_town, town_data in filtered_settlements:
        print(f"{left_town} -> Population: {town_data[0]} citizens, Gold: {town_data[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
