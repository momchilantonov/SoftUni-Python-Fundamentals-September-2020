nums = int(input())

positive_list = []
negative_list = []

for num in range(nums):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

count_positives = len(positive_list)
sum_negative = sum(negative_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_negative}")
