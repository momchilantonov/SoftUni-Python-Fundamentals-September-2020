needed_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
stop_loop = False

while True:
    if stop_loop:
        break
    items = input().lower().split(" ")
    for i in range(0, len(items), 2):
        key = items[i+1]
        val = int(items[i])
        if key in needed_items:
            needed_items[key] += val
            if needed_items[key] >= 250:
                stop_loop = True
                break
        elif key in junk_items:
            junk_items[key] += val
        else:
            junk_items[key] = val

if needed_items["shards"] >= 250:
    needed_items["shards"] -= 250
    print("Shadowmourne obtained!")
elif needed_items["fragments"] >= 250:
    needed_items["fragments"] -= 250
    print("Valanyr obtained!")
elif needed_items["motes"] >= 250:
    needed_items["motes"] -= 250
    print("Dragonwrath obtained!")

values_items = set(needed_items.values())

if len(values_items) == len(needed_items):
    sorted_items = dict(sorted(needed_items.items(), key=lambda x: -x[1]))
else:
    sorted_items = dict(sorted(needed_items.items(), key=lambda x: (-x[1], x[0])))

for k, v in sorted_items.items():
    print(f"{k}: {v}")

sorted_junk = dict(sorted(junk_items.items(), key=lambda x: x[0]))

for kj, vj in sorted_junk.items():
    print(f"{kj}: {vj}")
