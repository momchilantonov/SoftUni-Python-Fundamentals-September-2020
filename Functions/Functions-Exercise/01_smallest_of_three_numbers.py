import sys


def smallest_one(num_1, num_2, num_3):
    smallest_num = sys.maxsize
    if num_1 < smallest_num:
        smallest_num = num_1
    if num_2 < smallest_num:
        smallest_num = num_2
    if num_3 < smallest_num:
        smallest_num = num_3
    return smallest_num


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest_one(num_1, num_2, num_3))
