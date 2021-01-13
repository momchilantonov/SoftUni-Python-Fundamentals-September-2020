nums_as_string = input()

nums_as_list = nums_as_string.split()

for i in range(len(nums_as_list)):
    nums_as_list[i] = - int(nums_as_list[i])

print(nums_as_list)
