product_dict = {}

while True:
    product = input()
    if product == "stop":
        break

    qty = int(input())
    if product not in product_dict:
        product_dict[product] = qty
    else:
        product_dict[product] += qty

for key, val in product_dict.items():
    print(f"{key} -> {val}")
