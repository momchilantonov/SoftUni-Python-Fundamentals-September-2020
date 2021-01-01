def collect(journal, item):
    if item not in journal:
        journal.append(item)
    return journal


def drop(journal, item):
    if item in journal:
        journal.remove(item)
    return journal


def combine(journal, items):
    [old_item, new_item] = items.split(":")
    for i in range(len(journal)):
        if journal[i] == old_item:
            journal.insert(i+1, new_item)
    return journal


def renew(journal, item):
    for i in range(len(journal)):
        if journal[i] == item:
            journal.pop(i)
            journal.append(item)
    return journal


journal_of_items = input().split(", ")

while True:
    commands = input()
    if commands == "Craft!":
        break
    [command, item] = commands.split(" - ")
    if command == "Collect":
        journal_of_items = collect(journal_of_items, item)
    elif command == "Drop":
        journal_of_items = drop(journal_of_items, item)
    elif command == "Combine Items":
        journal_of_items = combine(journal_of_items, item)
    elif command == "Renew":
        renew(journal_of_items, item)

print(", ".join(journal_of_items))
