food = input().split(" ")

products_list = {}

for i in range(0, len(food), 2):
    key = food[i]
    val = int(food[i+1])
    products_list[key] = val

print(products_list)
