nums = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for num in range(nums):
    new_num = int(input())
    if new_num % 2 == 0 or new_num == 0:
        even_list.append(new_num)
    if not new_num % 2 == 0:
        odd_list.append(new_num)
    if new_num >= 0:
        positive_list.append(new_num)
    if new_num < 0:
        negative_list.append(new_num)

operation = input()

if operation == 'even':
    print(even_list)
elif operation == 'odd':
    print(odd_list)
elif operation == 'negative':
    print(negative_list)
elif operation == 'positive':
    print(positive_list)



