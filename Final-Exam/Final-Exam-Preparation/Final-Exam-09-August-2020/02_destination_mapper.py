import re

destinations = input()

travel_points = 0

pattern = r"(?<=(?P<lb>[=/]))(?P<match>[A-Z]{1}[A-Za-z]{2,})(?=(?P=lb))"

valid_locations = re.finditer(pattern, destinations)

valid_destinations = [location.group() for location in valid_locations]

print(f"Destinations: {', '.join(valid_destinations)}")

for el in valid_destinations:
    travel_points += len(el)

print(f"Travel Points: {travel_points}")
