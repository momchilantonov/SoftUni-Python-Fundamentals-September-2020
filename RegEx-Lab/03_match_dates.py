import re

date = input()

pattern = r"\b(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b"

valid_dates = re.finditer(pattern, date)

for valid_date in valid_dates:
    result = valid_date.groupdict()
    print(f"Day: {result['day']}, Month: {result['month']}, Year: {result['year']}")
