products_on_stock = {}

while True:
    products = input()
    if products == "statistics":
        break

    product, qty = products.split(": ")
    qty = int(qty)
    if product in products_on_stock:
        products_on_stock[product] += qty
    else:
        products_on_stock[product] = qty

print("Products in stock:")
for p, q in products_on_stock.items():
    print(f"- {p}: {q}")
print(f"Total Products: {len(products_on_stock)}")
print(f"Total Quantity: {sum(products_on_stock.values())}")
