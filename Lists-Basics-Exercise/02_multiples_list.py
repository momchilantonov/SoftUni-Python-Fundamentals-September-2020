factor = int(input())
count = int(input())

empty_list = []

for i in range(count):
    empty_list.append(i)

for i in range(len(empty_list)):
    empty_list[i] = (i+1) * factor

print(empty_list)
