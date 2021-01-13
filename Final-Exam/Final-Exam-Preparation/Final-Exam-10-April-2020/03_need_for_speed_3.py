num_cars = int(input())

cars_data = {}


def drive(car, type, distance, fuel):
    if car[type]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
        return car
    else:
        car[type]["fuel"] -= fuel
        car[type]["mileage"] += distance
        print(f"{type} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car[type]["mileage"] >= 100000:
            print(f"Time to sell the {type}!")
            del car[type]
        return car


def refuel(car, type, fuel):
    req_fuel = 75-car[type]["fuel"]
    car[type]["fuel"] += fuel
    if car[type]["fuel"] >= 75:
        car[type]["fuel"] = 75
        print(f"{type} refueled with {req_fuel} liters")
        return car
    else:
        print(f"{type} refueled with {fuel} liters")
        return car


def revert(car, type, kilometers):
    car[type]["mileage"] -= kilometers
    if car[type]["mileage"] < 10000:
        car[type]["mileage"] = 10000
        return car
    else:
        print(f"{type} mileage decreased by {kilometers} kilometers")
        return car


for cars in range(num_cars):
    [type, mileage, fuel] = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars_data[type] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        break

    action = command.split(" : ")

    if action[0] == "Drive":
        cars_data = drive(cars_data, action[1], int(action[2]), int(action[3]))
    elif action[0] == "Refuel":
        cars_data = refuel(cars_data, action[1], int(action[2]))
    elif action[0] == "Revert":
        cars_data = revert(cars_data, action[1], int(action[2]))

filtered_cars = sorted(cars_data.items(), key=lambda x: (-x[1]["mileage"], x[0]))

for car, data in filtered_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")

