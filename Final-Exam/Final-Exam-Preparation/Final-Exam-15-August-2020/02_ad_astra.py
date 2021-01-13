import re

txt = input()

pattern = r"(?P<symb>[\|#])(?P<name>[a-zA-z ]{1,})(?P=symb)" \
          r"(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})(?P=symb)" \
          r"(?P<cal>[0-9]{1,5})(?P=symb)"

all_food = re.finditer(pattern, txt)
cal_sum = sum([int(val.groupdict()["cal"]) for val in all_food])
days = cal_sum // 2000

print(f"You have food to last you for: {days} days!")

result = re.findall(pattern, txt)

for val in result:
    print(f"Item: {val[1]}, Best before: {val[2]}, Nutrition: {val[3]}")

