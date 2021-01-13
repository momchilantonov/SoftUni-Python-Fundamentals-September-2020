import re

numbers = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = re.finditer(pattern, numbers)

for number in valid_numbers:
    print(number.group(), end=" ")

