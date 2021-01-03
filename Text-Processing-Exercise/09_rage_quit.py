line = input()

current_rage = ""
final_rage = ""
index = 0

while index < len(line):
    if not line[index].isdigit():
        current_rage += line[index]
        index += 1
    else:
        number = ""
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1
        number = int(number)
        final_rage += current_rage.upper() * number
        current_rage = ""

print(f"Unique symbols used: {len(set(final_rage))}")
print(final_rage)
