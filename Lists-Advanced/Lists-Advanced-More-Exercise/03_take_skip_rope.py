message = input()

num_list = []
non_num_list = []
skip_list = []
take_list = []
result = []

for ch in message:
    if ch.isdigit():
        num_list.append(int(ch))
    else:
        non_num_list.append(ch)

for n in range(len(num_list)):
    if n % 2 == 0:
        take_list.append(num_list[n])
    else:
        skip_list.append(num_list[n])

skip_i = 0

for i1, i2 in zip(skip_list, take_list):
    for i in non_num_list[skip_i:skip_i+i2]:
        result.append(i)
    skip_i += i1+i2

print(f"{''.join(result)}")
