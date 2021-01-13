import re

txt = input()
all_numbers = []

while True:
    if len(txt) == 0:
        break
    else:
        pattern = r"\d+"
        valid_number = re.finditer(pattern, txt)
        for n in valid_number:
            all_numbers.append(n.group())
        txt = input()

for number in all_numbers:
    print(number, end=" ")
