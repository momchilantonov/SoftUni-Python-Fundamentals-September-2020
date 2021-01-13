a = int(input())
b = int(input())

first_list = [a, b]
second_list = first_list[::-1]

print("Before:")
print(f"a = {first_list[0]}")
print(f"b = {first_list[1]}")
print("After:")
print(f"a = {second_list[0]}")
print(f"b = {second_list[1]}")
