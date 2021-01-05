number_of_heroes = int(input())
heroes_data = {}


def cast_spell(name, mana, spell, mana_availability):
    if mana <= mana_availability:
        mana_availability -= mana
        print(f"{name} has successfully cast {spell} and now has {mana_availability} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")
    return mana_availability


def take_dmg(name, dmg, attacker, health_availability):
    health_availability[name]["HP"] -= dmg
    if health_availability[name]["HP"] > 0:
        print(f"{name} was hit for {dmg} HP by {attacker} and now has {health_availability[name]['HP']} HP left!")
        return health_availability
    else:
        del health_availability[name]
        print(f"{name} has been killed by {attacker}!")
        return health_availability


def recharge(name, mana, mana_availability):
    needed_mana = 200-mana_availability
    mana_availability += mana
    if mana_availability >= 200:
        mana_availability = 200
        print(f"{name} recharged for {needed_mana} MP!")
        return mana_availability
    else:
        print(f"{name} recharged for {mana} MP!")
        return mana_availability


def heal(name, health, health_availability):
    needed_health = 100-health_availability
    health_availability += health
    if health_availability >= 100:
        health_availability = 100
        print(f"{name} healed for {needed_health} HP!")
        return health_availability
    else:
        print(f"{name} healed for {health} HP!")
        return health_availability


for _ in range(number_of_heroes):
    [hero_name, hp_points, mana_points] = input().split(" ")
    hp_points = int(hp_points)
    mana_points = int(mana_points)
    heroes_data[hero_name] = {"HP": hp_points, "MP": mana_points}

while True:
    command = input()
    if command == "End":
        break

    action = command.split(" - ")
    current_action = action[0]
    current_name = action[1]
    current_value = int(action[2])
    if current_action == "CastSpell":
        current_spell = action[3]
        heroes_data[current_name]["MP"] = \
            cast_spell(current_name, current_value, current_spell, heroes_data[current_name]["MP"])
    elif current_action == "TakeDamage":
        current_attacker = action[3]
        heroes_data = \
            take_dmg(current_name, current_value, current_attacker, heroes_data)
    elif current_action == "Recharge":
        heroes_data[current_name]["MP"] = \
            recharge(current_name, current_value, heroes_data[current_name]["MP"])
    elif current_action == "Heal":
        heroes_data[current_name]["HP"] = \
            heal(current_name, current_value, heroes_data[current_name]["HP"])

filtered_heroes = sorted(heroes_data.items(), key=lambda x: (-x[1]["HP"], x[0]))

for hero, data in filtered_heroes:
    print(hero)
    print(f"HP: {data['HP']}")
    print(f"MP: {data['MP']}")
