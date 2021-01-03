[text_1, text_2] = input().split(" ")
text_1_nums = [ord(ch) for ch in text_1]
text_2_nums = [ord(ch) for ch in text_2]
total_sum = 0

if len(text_1_nums) > len(text_2_nums):
    needed_indices = len(text_1_nums)-len(text_2_nums)
    for _ in range(needed_indices):
        text_2_nums.append(1)
elif len(text_1_nums) < len(text_2_nums):
    needed_indices = len(text_2_nums)-len(text_1_nums)
    for _ in range(needed_indices):
        text_1_nums.append(1)

for i in range(len(text_1_nums)):
    total_sum += text_1_nums[i] * text_2_nums[i]

print(total_sum)
