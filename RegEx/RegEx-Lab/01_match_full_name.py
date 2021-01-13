import re

names = input()

pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

valid_names = re.findall(pattern, names)

print(*valid_names, sep=" ")
