numbers = input().split()
n_removes = int(input())

numbers_list = [int(numbers[i]) for i in range(len(numbers))]

for removes in range(n_removes):
    numbers_list.remove(min(numbers_list))

print(numbers_list)
