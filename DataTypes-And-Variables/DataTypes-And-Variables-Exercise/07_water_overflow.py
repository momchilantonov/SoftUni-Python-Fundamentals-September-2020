n = int(input())

capacity = 255
liters_in_tank = 0

for i in range(n):
    liters = int(input())
    liters_in_tank += liters

    if liters_in_tank > 255:
        liters_in_tank -= liters
        print('Insufficient capacity!')

print(liters_in_tank)
