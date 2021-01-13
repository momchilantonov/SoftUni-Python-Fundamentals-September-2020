from math import ceil

persons = int(input())
capacity = int(input())

courses = 0

if persons <= capacity:
    courses += 1
elif persons > capacity:
    courses = ceil(persons / capacity)

print(courses)
