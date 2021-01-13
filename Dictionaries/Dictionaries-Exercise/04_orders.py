product_price = {}
product_qty = {}

while True:
    command = input()
    if command == "buy":
        break

    product_data = command.split(" ")
    product = product_data[0]
    price = float(product_data[1])
    qty = int(product_data[2])

    if product not in product_qty:
        product_qty[product] = qty
        product_price[product] = price
    else:
        product_qty[product] += qty
        product_price[product] = price

for product, price in product_price.items():
    total_price = price * product_qty[product]
    print(f"{product} -> {total_price:.2f}")
