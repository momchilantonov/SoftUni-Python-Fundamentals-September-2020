import re

phone_numbers = input()

pattern = r"\+359(?P<sep>\s|-)2(?P=sep)\d{3}(?P=sep)\d{4}\b"

valid_phone_numbers = re.finditer(pattern, phone_numbers)

valid_phone_numbers = [p.group() for p in valid_phone_numbers]

print(*valid_phone_numbers, sep=", ")


