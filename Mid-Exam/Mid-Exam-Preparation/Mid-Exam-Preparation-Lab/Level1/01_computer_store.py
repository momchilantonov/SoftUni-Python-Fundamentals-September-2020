sum_of_prices = 0

while True:
    price = input()
    if price == "special" or price == "regular":
        break

    price = float(price)
    if price < 0:
        print("Invalid price!")
    else:
        sum_of_prices += price

sum_with_taxes = sum_of_prices * 1.2
taxes = sum_with_taxes-sum_of_prices

if price == "special":
    sum_with_taxes = sum_with_taxes * 0.9
else:
    sum_with_taxes = sum_with_taxes
if sum_of_prices == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_of_prices:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {sum_with_taxes:.2f}$")
