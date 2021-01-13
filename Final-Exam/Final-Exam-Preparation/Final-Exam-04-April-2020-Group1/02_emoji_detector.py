import re

txt = input()
threshold = 1

digits = re.findall(r"\d", txt)
emojis = re.findall(r"\*\*[A-Z][a-z]{2,}\*\*|::[A-Z][a-z]{2,}::", txt)
emojis_for_print = []

for digit in digits:
    digit = int(digit)
    threshold *= digit

print(f"Cool threshold: {threshold}")

for index in range(len(emojis)):
    emoji_sum = 0
    for element in emojis[index]:
        if element == ':' or element == "*":
            continue
        else:
            emoji_sum += ord(element)
    if emoji_sum > threshold:
        emojis_for_print.append(emojis[index])

print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis_for_print:
    print(emoji)
