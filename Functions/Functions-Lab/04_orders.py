def order_price(product, qty):
    result = 0
    if product == "coffee":
        result = qty * 1.5
    elif product == "coke":
        result = qty * 1.4
    elif product == "water":
        result = qty
    elif product == "snacks":
        result = qty * 2
    return f"{result:.2f}"


product_type = input()
product_qty = int(input())

print(order_price(product_type, product_qty))
