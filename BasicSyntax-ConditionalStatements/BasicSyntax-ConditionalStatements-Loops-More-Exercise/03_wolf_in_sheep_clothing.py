animals = input().split(", ")

for animal_index in range(len(animals)):
    if animals[animal_index] == "wolf":
        if animals[animal_index] == animals[-1]:
            print("Please go away and stop eating my sheep")
        else:
            sheep_num = len(animals[animal_index+1:])
            print(f"Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!")
