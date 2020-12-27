budget = float(input())
flour_price = float(input())

cozonac_qty = 0
colored_eggs = 0
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
cozonac_price = flour_price + eggs_price + milk_price

while budget > cozonac_price:
    cozonac_qty += 1
    budget -= cozonac_price
    colored_eggs += 3
    if cozonac_qty % 3 == 0:
        colored_eggs -= cozonac_qty - 2

print(f'You made {cozonac_qty} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
