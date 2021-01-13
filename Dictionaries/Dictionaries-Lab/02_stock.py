products_on_stock = input().split(" ")
products_for_search = input().split(" ")
products_list = {}

for i in range(0, len(products_on_stock), 2):
    key = products_on_stock[i]
    val = int(products_on_stock[i+1])
    products_list[key] = val

for product in products_for_search:
    if product in products_list:
        print(f"We have {products_list[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
