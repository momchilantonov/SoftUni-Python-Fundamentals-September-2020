numbers = input().split(",")
n_beggars = int(input())

numbers = [int(numbers[i]) for i in range(len(numbers))]

beggars_total_sum = []

for beggar in range(n_beggars):
    beggar_sum = []
    for index in range(beggar, len(numbers), n_beggars):
        beggar_sum.append(numbers[index])
    temp_sum = sum(beggar_sum)
    beggars_total_sum.append(temp_sum)

print(beggars_total_sum)
