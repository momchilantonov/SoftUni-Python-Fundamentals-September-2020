nums = int(input())
word = input()

result_1 = []
result_2 = []

for num in range(nums):
    new_word = input()
    result_1.append(new_word)
    if word in new_word:
        result_2.append(new_word)

print(result_1)
print(result_2)
