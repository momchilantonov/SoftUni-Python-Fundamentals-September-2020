import re

furniture_names = []
total_cost = 0

while True:
    data = input()
    if data == "Purchase":
        break

    pattern = r"^>{2}(?P<name>[A-Za-z]+)<{2}(?P<price>\d+\.?\d+)!(?P<qty>\d+)$"

    furniture_data = re.match(pattern, data)
    if furniture_data:
        furniture_match = furniture_data.groupdict()
        furniture_names.append(furniture_match["name"])
        total_cost += float(furniture_match["price"]) * int(furniture_match["qty"])

print("Bought furniture:")

for furniture in furniture_names:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")

# import re
#
# furniture_names = {"names": []}
# furniture_prices = {"price": []}
# furniture_qty = {"qty": []}
#
# while True:
#     data = input()
#     if data == "Purchase":
#         break
#
#     pattern = r"^>{2}(?P<name>[A-Za-z]+)<{2}(?P<price>\d+\.?\d+)!(?P<qty>\d+)$"
#
#     furniture_data = re.finditer(pattern, data)
#
#     for furniture in furniture_data:
#         furniture_names["names"] += [furniture["name"]]
#         furniture_prices["price"] += ([furniture["price"]])
#         furniture_qty["qty"] += [furniture["qty"]]
#
# print("Bought furniture:")
#
# for val in furniture_names.values():
#     for v in val:
#         print(v)
#
# total_price = [float(ch) for ch in furniture_prices["price"]]
# total_qty = [int(ch) for ch in furniture_qty["qty"]]
# total_cost = 0
#
# for i in range(len(total_price)):
#     total_cost += total_price[i] * total_qty[i]
#
# print(f"Total money spend: {total_cost:.2f}")
