def collect(items, item):
    if item not in items:
        items.append(item)
    return items


def drop(items, item):
    if item in items:
        items.remove(item)
    return items


def combine_items(items, item):
    [old_item, new_item] = item.split(":")
    for i in range(len(items)):
        if items[i] == old_item:
            items.insert(i+1, new_item)
    return items


def renew(items, item):
    for i in range(len(items)):
        if items[i] == item:
            items.pop(i)
            items.append(item)
    return items


items = input().split(", ")

while True:
    commands = input()
    if commands == "Craft!":
        break
    [command, item] = commands.split(" - ")
    if command == "Collect":
        items = collect(items, item)
    elif command == "Drop":
        items = drop(items, item)
    elif command == "Combine Items":
        items = combine_items(items, item)
    elif command == "Renew":
        renew(items, item)

print(", ".join(items))
