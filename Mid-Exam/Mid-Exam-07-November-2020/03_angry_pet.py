price_rating = [int(i) for i in input().split(" ")]
entry_point = int(input())
items_type = input()
price_rating_type = input()

left_items = price_rating[:entry_point]
right_items = price_rating[entry_point+1:]

if price_rating_type == "positive":
    left_items = [i for i in left_items if i >= 0]
elif price_rating_type == "negative":
    left_items = [i for i in left_items if i < 0]
elif price_rating_type == "all":
     left_items = left_items

if items_type == "expensive":
    left_items = [i for i in left_items if i >= price_rating[entry_point]]
elif items_type == "cheap":
    left_items = [i for i in left_items if i < price_rating[entry_point]]

left_sum = sum(left_items)

if price_rating_type == "positive":
    right_items = [i for i in right_items if i >= 0]
elif price_rating_type == "negative":
    right_items = [i for i in right_items if i < 0]
elif price_rating_type == "all":
     right_items = right_items

if items_type == "expensive":
    right_items = [i for i in right_items if i >= price_rating[entry_point]]
elif items_type == "cheap":
    right_items = [i for i in right_items if i < price_rating[entry_point]]

right_sum = sum(right_items)

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
elif right_sum > left_sum:
    print(f"Right - {right_sum}")
