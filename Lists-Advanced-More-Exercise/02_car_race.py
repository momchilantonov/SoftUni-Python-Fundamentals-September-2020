time_list = [int(el) for el in input().split(" ")]

left_racer = time_list[:len(time_list) // 2]
right_racer = time_list[-1:len(time_list) // 2:-1]


def calc_time(racer_time):
    total_time = 0
    for t in racer_time:
        if t > 0:
            total_time += t
        else:
            total_time = total_time * 0.8
    return total_time


if calc_time(left_racer) > calc_time(right_racer):
    print(f"The winner is right with total time: {calc_time(right_racer):.1f}")
else:
    print(f"The winner is left with total time: {calc_time(left_racer):.1f}")
