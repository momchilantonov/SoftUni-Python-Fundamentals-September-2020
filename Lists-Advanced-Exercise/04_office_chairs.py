number_of_rooms = int(input())

total_free_chairs = 0
rooms_count = 0

for i in range(1, number_of_rooms + 1):
    chairs_data, taken_chairs = input().split(" ")
    taken_chairs = int(taken_chairs)
    needed_chairs = 0
    if len(chairs_data) < taken_chairs:
        needed_chairs += taken_chairs - len(chairs_data)
        rooms_count -= 1
        print(f"{needed_chairs} more chairs needed in room {i}")
        continue
    elif len(chairs_data) > taken_chairs or len(chairs_data) == taken_chairs:
        total_free_chairs += len(chairs_data) - taken_chairs
        rooms_count += 1
if rooms_count == number_of_rooms:
    print(f"Game On, {total_free_chairs} free chairs left")
